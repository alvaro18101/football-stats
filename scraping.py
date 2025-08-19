from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.google.com/search?q=barcelona+vs&oq=&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIGCAAQRRg5MgYIARBFGDsyDAgCEC4YJxiABBiKBTISCAMQABhDGIMBGLEDGIAEGIoFMgwIBBAAGEMYgAQYigUyDAgFEAAYQxiABBiKBTIGCAYQRRg9MgYIBxBFGDzSAQgxMzkzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8#sie=m;/g/11yfnc0n2f;2;/m/09gqx;ms;fp;1;;;'
driver.get(url=url)
time.sleep(5)

# Web scraping
html = driver.page_source
driver.quit()

soup  = BeautifulSoup(html, 'html.parser')

championship = soup.find('span', {'class': 'imso-loa imso-ln'}).text
# championship = soup.find('span', {'class': 'imso-hide-overflow'})
# date = 

result1 = soup.find('div', {'class': 'imso_mh__l-tm-sc imso_mh__scr-it imso-light-font'}).text
result2 = soup.find('div', {'class': 'imso_mh__r-tm-sc imso_mh__scr-it imso-light-font'}).text

team_stats = soup.find_all('tr', {'class': 'MzWkAb'})
stats_1 = []
stats_2 = []

for i in team_stats:
    team_stats_contents = i.contents
    stats_1.append(team_stats_contents[0].text)
    stats_2.append(team_stats_contents[2].text)


goals_info_1 = ''
goals_info_2 = ''
if int(result1)>0:
    goals_info_1 = soup.find('div', {'class': 'imso_gs__tgs imso_gs__left-team'})
if int(result2)>0:
    goals_info_2 = soup.find('div', {'class': 'imso_gs__tgs imso_gs__right-team'})

# print()
# print(type(goals_info_1))
print((goals_info_2.text))

if int(stats_1[6]) + int(stats_1[7]) + int(stats_2[6]) + int(stats_2[7]) > 0:
    cards_info = soup.find('div', {'class': 'imso_gs__cs-cont imso-medium-font'})

print(cards_info.text)