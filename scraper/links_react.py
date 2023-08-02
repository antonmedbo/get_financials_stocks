from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re


def get_links_from_react_page(company_config):
    # Automatically download and install chromedriver
    webdriver_path = ChromeDriverManager().install()

    # Define the path to the Chrome application
    chrome_app_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    # Define options for Chrome
    chrome_options = Options()
    chrome_options.binary_location = chrome_app_path

    # Define the service
    webdriver_service = Service(webdriver_path)

    # Create new instance of chrome
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    url = 'https://www.alfalaval.se/investerare/publikationer/kvartalsinformation/'

    # get the page
    driver.get(url)

    # let JavaScript load
    driver.implicitly_wait(10)  # waits up to 10 seconds for elements to appear

    html = driver.page_source

    # parse with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    pattern = re.compile(r'https://www.alfalaval.com/globalassets/documents/.*\.xlsx')

    links = soup.find_all('a', href=pattern)

    # quit the driver
    driver.quit()

    return links
