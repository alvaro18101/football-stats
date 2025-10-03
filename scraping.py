from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import datetime
import calendar

def fix_date(date):
    date = date.split(', ')[-1]
    if date == 'Hoy':
        return f'{datetime.date.today().day}/{datetime.date.today().month}'
    
    if date == 'Ayer':
        if datetime.date.today().day != 1:
            return f'{datetime.date.today().day - 1}/{datetime.date.today().month}'
        else:
            year = datetime.date.today().year
            month = datetime.date.today().month
            _, days_in_month = calendar.monthrange(year, month)
            return f'{days_in_month}/{datetime.date.today().month}'
    return date


def scrape_match(url):
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=service, options=options)
    # url = 'https://www.google.com/search?q=barcelona+vs&oq=&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIGCAAQRRg5MgYIARBFGDsyDAgCEC4YJxiABBiKBTISCAMQABhDGIMBGLEDGIAEGIoFMgwIBBAAGEMYgAQYigUyDAgFEAAYQxiABBiKBTIGCAYQRRg9MgYIBxBFGDzSAQgxMzkzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#sie=m;/g/11yfnc0n2f;2;/m/09gqx;ms;fp;1;;;'

    driver.get(url=url)
    time.sleep(5)

    # Web scraping
    html = driver.page_source
    driver.quit()

    soup  = BeautifulSoup(html, 'html.parser')

    teams_name = soup.find_all('div', {'class': 'liveresults-sports-immersive__hide-element'})
    team_1_name = teams_name[0].text
    team_2_name = teams_name[1].text

    championship = soup.find('span', {'class': 'imso-loa imso-ln'}).text
    date = soup.find('div', {'class': 'imso-hide-overflow'}).contents[-1].text
    date = fix_date(date)

    result1 = soup.find('div', {'class': 'imso_mh__l-tm-sc imso_mh__scr-it imso-light-font'}).text
    result2 = soup.find('div', {'class': 'imso_mh__r-tm-sc imso_mh__scr-it imso-light-font'}).text

    team_stats = soup.find_all('tr', {'class': 'MzWkAb'})
    stats_1 = []
    stats_2 = []
    stats_name = soup.find_all('th', {'class': 'JmSkkf'})

    for i in team_stats:
        team_stats_contents = i.contents
        stats_1.append(team_stats_contents[0].text)
        stats_2.append(team_stats_contents[2].text)


    goals_info_1 = ''
    goals_info_2 = ''
    goals_list_1 = []
    goals_list_2 = []

    if int(result1)>0:
        goals_info_1 = soup.find('div', {'class': 'imso_gs__tgs imso_gs__left-team'})
        for i in (goals_info_1.contents):
            goals_item_1 = []
            for j in i.contents:
                if j.text.replace('\xa0','') != '':
                    item = j.text.strip()
                    item = item.replace('\xa0', ' ')
                    goals_item_1.append(item)
            goals_list_1.append(goals_item_1)
    if int(result2)>0:
        goals_info_2 = soup.find('div', {'class': 'imso_gs__tgs imso_gs__right-team'})
        for i in (goals_info_2.contents):
            goals_item_2 = []
            for j in i.contents:
                if j.text.replace('\xa0','') != '':
                    item = j.text.strip()
                    item = item.replace('\xa0', ' ')
                    goals_item_2.append(item)
            goals_list_2.append(goals_item_2)

    if int(stats_1[6]) + int(stats_1[7]) + int(stats_2[6]) + int(stats_2[7]) > 0:
        cards_info = soup.find('div', {'class': 'imso_gs__cs-cont imso-medium-font'})

    data_team_1 = [1, date, championship, team_2_name, 'Home', result1, result2, goals_list_1]
    data_team_2 = [1, date, championship, team_1_name, 'Away', result2, result1, goals_list_2]
    data_team_1.extend(stats_1)
    data_team_2.extend(stats_2)

    print('---Successful scraping---')
    return team_1_name, data_team_1, team_2_name, data_team_2