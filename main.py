import openpyxl
import psycopg2
from utils.check import get_date, three_months, which_metric, get_multiplier
from pprint import pprint
from utils.check_document_name import year_from_name
from scraper.ABB_scraper import get_excel_files_ABB

get_excel_files_ABB()
