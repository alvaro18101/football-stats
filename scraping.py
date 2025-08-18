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

result1 = soup.find('div', {'class': 'imso_mh__l-tm-sc imso_mh__scr-it imso-light-font'}).text
result2 = soup.find('div', {'class': 'imso_mh__r-tm-sc imso_mh__scr-it imso-light-font'}).text