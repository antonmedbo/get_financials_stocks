import requests
import io
from openpyxl import load_workbook
from zipfile import BadZipFile
from extractor.get_data import from_excel

def get_data_from_xlsx(links, company_config):
    list_income_statements = []

    for link in links:
        url = link['href']

        if url.startswith("/"):
            url = company_config["base_url"] + url

        parent_tr = link.find_parent('tr')
        year = parent_tr.find('td').get_text(strip=True).split(' ')[1]

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