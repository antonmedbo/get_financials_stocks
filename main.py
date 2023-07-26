import openpyxl
import psycopg2
from utils.check import get_date, three_months, which_metric, get_multiplier
from pprint import pprint
from utils.check_document_name import year_from_name
from scraper.ABB_scraper import get_excel_files_ABB
import json
from datetime import datetime

list_income_statements = get_excel_files_ABB()

def datetime_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()
    
# Use json.dump to write data to a json file
with open('data.json', 'w') as f:
    json.dump(list_income_statements, f, default=datetime_converter, indent=4)