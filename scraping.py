from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    driver.get(url=url)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[8]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]')))

    # Web scraping
    html = driver.page_source

    soup  = BeautifulSoup(html, 'html.parser')

    team_name_1 = None
    team_name_2 = None
    try:
        team_name_1 = driver.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[8]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]')
        team_name_1 = team_name_1.text
        team_name_2 = driver.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[8]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/span[1]')
        team_name_2 = team_name_2.text
    except:
        print('Error scraping team names')    

    championship = None
    try:
        championship = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[8]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]")
        championship = championship.text
    except:
        print('Error scraping championship')

    date = None
    try:
        date = soup.find('div', {'class': 'imso-hide-overflow'}).contents[-1].text
        date = fix_date(date)
    except:
        print('Error scraping date')

    result1 = None
    result2 = None
    try:
        result1 = soup.find('div', {'class': 'imso_mh__l-tm-sc imso_mh__scr-it imso-light-font'}).text
        result2 = soup.find('div', {'class': 'imso_mh__r-tm-sc imso_mh__scr-it imso-light-font'}).text
    except:
        print('Error scraping results')

    team_stats_table = None
    stats_1 = []
    stats_2 = []
    try:
        team_stats_table = driver.find_element(By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[8]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/table[1]')
        team_stats = team_stats_table.find_elements(By.TAG_NAME, 'tr')
        team_stats = team_stats[1:]
        for i in range(len(team_stats)):
            children = team_stats[i].find_elements(By.XPATH, "./*")
            stats_1.append(children[0].text)
            stats_2.append(children[2].text)
    except:
        print('Error scraping stats')

    print(championship)
    print(f'Fecha: {date}')
    print()
    print(f'{team_name_1} {result1} - {result2} {team_name_2}')
    print()
    print(team_stats_table.text)

    goals_info_1 = ''
    goals_info_2 = ''
    goals_list_1 = []
    goals_list_2 = []

    if int(result1) > 0:
        goals_info_1 = soup.find('div', {'class': 'imso_gs__tgs imso_gs__left-team'})
        for i in (goals_info_1.contents):
            goals_item_1 = []
            for j in i.contents:
                if j.text.replace('\xa0','') != '':
                    item = j.text.strip()
                    item = item.replace('\xa0', ' ')
                    goals_item_1.append(item)
            goals_list_1.append(goals_item_1)
    if int(result2) > 0:
        goals_info_2 = soup.find('div', {'class': 'imso_gs__tgs imso_gs__right-team'})
        for i in (goals_info_2.contents):
            goals_item_2 = []
            for j in i.contents:
                if j.text.replace('\xa0','') != '':
                    item = j.text.strip()
                    item = item.replace('\xa0', ' ')
                    goals_item_2.append(item)
            goals_list_2.append(goals_item_2)
    print()
    for player, minute in goals_list_1:
        print(f'{player}: {minute}')
    # if int(stats_1[6]) + int(stats_1[7]) + int(stats_2[6]) + int(stats_2[7]) > 0:
    #     cards_info = soup.find('div', {'class': 'imso_gs__cs-cont imso-medium-font'})

    data_team_1 = [1, date, championship, team_name_2, 'Home', result1, result2, goals_list_1]
    data_team_2 = [1, date, championship, team_name_1, 'Away', result2, result1, goals_list_2]
    data_team_1.extend(stats_1)
    data_team_2.extend(stats_2)
    driver.quit()
    print()
    print('---Successful scraping---')
    return team_name_1, data_team_1, team_name_2, data_team_2

if __name__ == '__main__':
    test_url = 'https://www.google.com/search?q=partidos+de+fc+barcelona&gs_lcrp=EgZjaHJvbWUqEwgAEEUYJxg7GEYY_QEYgAQYigUyEwgAEEUYJxg7GEYY_QEYgAQYigUyBggBEEUYOTIGCAIQRRg7MgwIAxAjGCcYgAQYigUyDAgEEAAYQxiABBiKBTIGCAUQRRg8MgYIBhBFGDwyBggHEEUYPNIBBzQ2MGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8&si=AL3DRZGGPnnVaiK67YqdUfewzBcS-upM6QijhdUU6Jr8AWsjr8v9CvA-SnNnnxtCTH-Iycrz5Hfiy-o4IHk920D1F5HguzudSJBINLsQJs59tzpsV_DoE3teFj2StyQBu6wTFVQRHxAkZnNilYk5UX14zeC2J8cvyMEij66lv5a54Lb3tXTNH6EwDjyO9HmSby9uktlmw334vuaRUSjGAk8JkgNu1ms_j6cVIbsxZLNpcq6GWPT4U0U%3D&ictx=1&ved=2ahUKEwiNvb7TyK6SAxW1ALkGHR5dJN8Qk8EMegQIPRAC#sie=m;/g/11xt5lg49k;2;/m/0c1q0;dt;fp;1;;;;-1'

    scrape_match(test_url)