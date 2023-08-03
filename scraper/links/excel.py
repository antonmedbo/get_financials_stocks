import requests
import io
from openpyxl import load_workbook
from zipfile import BadZipFile
from extractor.get_data import from_excel
from pprint import pprint
from extractor.xlsx.get_positions import quarters, metrics
from extractor.xlsx.get_data import from_sheet

def get_data_from_xlsx(url, company, config, year):
    list_income_statements = []

    if url.startswith("/"):
        url = config["base_url"] + url

    response = requests.get(url)
    content = response.content

    try:
        print(url)
        workbook = load_workbook(filename=io.BytesIO(content))
        sheet = workbook.active

        index_quarters = quarters(workbook)
        index_metrics = metrics(company, workbook)

        # complete_data = from_sheet(index_quarters, workbook)



        # income_statement = from_excel(sheet, index_quarters)

        # list_income_statements.append(income_statement)

    except BadZipFile:
        print(f"Invalid or corrupted file: {url}")
        
    return list_income_statements