import io
import json
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from zipfile import BadZipFile
from extracter.get_data import from_excel

def get_excel_files(company_config):
    list_income_statements = []
    response = requests.get(company_config["results_url"])
    soup = BeautifulSoup(response.content, 'html.parser')

    # Use the link pattern from the configuration
    links = soup.find_all('a', text=lambda text: text and company_config["link_pattern"] in text.lower())

    for link in links:
        url = link['href']

        if url.startswith("/"):
            url = company_config["base_url"] + url

        parent_tr = link.find_parent('tr')
        year = parent_tr.find('td').get_text(strip=True).split(' ')[1]

        print(url)

        response = requests.get(url)
        content = response.content

        try:
            workbook = load_workbook(filename=io.BytesIO(content))
            sheet = workbook.active

            income_statement = from_excel(sheet, year)

            list_income_statements.append(income_statement)
        except BadZipFile:
            print(f"Invalid or corrupted file: {url}")
    
    return list_income_statements

