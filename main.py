import openpyxl
import psycopg2
from utils.check import is_date, three_or_six_months, which_metric

# Load the Excel file
file_path = "/Users/antonmedboprivat/python/extract_financial_data/ABB-Q2-2023-financial-statements.xlsx"
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active
position_three_months = None
position_six_months = None

for row in sheet.iter_rows(values_only=True):

    for i, value in enumerate(row): 
        if three_or_six_months(str(value)) == "six_months":
            position_six_months = i
        elif three_or_six_months(str(value)) == "three_months":
            position_three_months = i
        if position_six_months and position_three_months:
            break
    

if position_three_months or position_three_months:
    for row in sheet.iter_rows(values_only=True):  
        for i in row: 
            if isinstance(i, str):
                print(which_metric(i))
