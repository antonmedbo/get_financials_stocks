import pandas as pd
from pprint import pprint
import json

def quarters(workbook):

# Load the Excel data into a pandas DataFrame
    df = pd.read_excel(workbook, engine='openpyxl')

    column_positions = {}

    for i, col in enumerate(df.columns):
        
        try:
            year, quarter = col.split()  # split column name into year and quarter
            if len(str(year)) == 4 and 1000 <= int(year) <= 9999:
                if year not in column_positions:  
                    column_positions[year] = {}
                column_positions[year][quarter] = i  # add quarter and column position to the year dict
        except: 
            print("not correct format:", col)
    
    return column_positions

def metrics(company, workbook):


    with open("/Users/antonmedboprivat/python/extract_financial_data/config/conversion_income_statements.json") as json_file:
        conversion = json.load(json_file)
        
    print(conversion)

    
