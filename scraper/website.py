from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

def get_links(company_config):
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

    url = company_config["results_url"]

    # get the page
    driver.get(url)

    # let JavaScript load
    driver.implicitly_wait(10)  # waits up to 10 seconds for elements to appear

    html = driver.page_source

    # parse with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    pattern = re.compile(company_config["link_pattern"], re.IGNORECASE)

    if company_config["method"] == "text":
        def match_pattern(text):
            return text and pattern.search(text) is not None
        links = soup.find_all(company_config["tag_name"], text=match_pattern)
    else:
        links = soup.find_all(lambda tag: tag.name == company_config['tag_name'] and tag.get(company_config['attr']) and pattern.search(tag.get(company_config['attr'])) is not None)

    # quit the driver
    driver.quit()

    return links
