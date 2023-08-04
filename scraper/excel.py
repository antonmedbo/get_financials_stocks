import requests
import io
from openpyxl import load_workbook
from zipfile import BadZipFile
from extractor.xlsx.get_positions import quarters, metrics
from extractor.xlsx.get_data import from_sheet
from pprint import pprint

def get_data_from_xlsx(url, company, config):

    if url.startswith("/"):
        url = config["base_url"] + url

    response = requests.get(url)
    content = response.content
    print(url)

    try:
        workbook = load_workbook(filename=io.BytesIO(content))

        index_quarters = quarters(workbook)

        pprint(index_quarters)
        
        # index_metrics = metrics(company, workbook)

        # income_statements_dataframe = from_sheet(company, index_quarters, index_metrics, workbook)

        # return income_statements_dataframe
    
    except BadZipFile:
        print(f"Invalid or corrupted file: {url}")
        
    