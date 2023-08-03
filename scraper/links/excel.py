import requests
import io
from openpyxl import load_workbook
from zipfile import BadZipFile
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

        income_statements_dataframe = from_sheet(index_quarters, index_metrics, workbook)

    except BadZipFile:
        print(f"Invalid or corrupted file: {url}")
        
    return income_statements_dataframe