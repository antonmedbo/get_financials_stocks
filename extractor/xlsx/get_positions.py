import pandas as pd
from pprint import pprint
import json
from dateutil import parser

def quarters(workbook):
    # Load the Excel data into a pandas DataFrame
    df = pd.read_excel(workbook, engine='openpyxl')

    column_positions = {}
    
    # First, check the header for dates
    for i, col in enumerate(df.columns):
        if isinstance(col, str):
            try:
                if col[:4].isdigit():  # check if the column name starts with a four-digit number
                    # "Year Quarter" format
                    year, quarter = col.split()  # split column name into year and quarter
                    if len(str(year)) == 4 and 1000 <= int(year) <= 9999:
                        if year not in column_positions:  
                            column_positions[year] = {}
                        column_positions[year][quarter] = i  # add quarter and column position to the year dict
                else:
                    # "Month. Day, Year" format
                    # Remove any .1 at the end of the column name
                    col = col.replace(".1", "")
                    
                    date = parser.parse(col)
                    year = str(date.year)
                    quarter = 'Q' + str((date.month - 1) // 3 + 1)  # convert month to quarter
                    
                    if year not in column_positions:  
                        column_positions[year] = {}
                        
                    if quarter not in column_positions[year]:
                        column_positions[year][quarter] = [i]  # create a list to handle duplicate columns
                    else:
                        column_positions[year][quarter].append(i)  # add column position to the list
            except:
                pass  # suppress error messages for columns that cannot be parsed

    # If no dates were found in the header, check the rows
    if not column_positions:
        for _, row in df.iterrows():
            for i, col in enumerate(row):
                if isinstance(col, str):
                    try:
                        if col[:4].isdigit():
                            year, quarter = col.split()
                            if len(str(year)) == 4 and 1000 <= int(year) <= 9999:
                                if year not in column_positions:  
                                    column_positions[year] = {}
                                column_positions[year][quarter] = i
                        else:
                            col = col.replace(".1", "")
                            date = parser.parse(col)
                            year = str(date.year)
                            quarter = 'Q' + str((date.month - 1) // 3 + 1)
                            if year not in column_positions:  
                                column_positions[year] = {}
                            if quarter not in column_positions[year]:
                                column_positions[year][quarter] = [i]
                            else:
                                column_positions[year][quarter].append(i)
                    except:
                        pass
            if column_positions:
                break
    
    return column_positions

def metrics(company, workbook):

    row_positions = {}

    with open("/Users/antonmedboprivat/python/extract_financial_data/config/conversion_income_statements.json") as json_file:
        conversion = json.load(json_file)
        
    df = pd.read_excel(workbook, engine='openpyxl')

    df_lower = df.applymap(lambda s: s.lower() if type(s) == str else s)
    
    for key, item in conversion.get(company).items():
        if len(key) > 2:
            row_index = df_lower[df_lower.eq(key).any(axis=1)].index.tolist()
            if item not in row_positions:
                row_positions[item] = row_index[0]
    return row_positions
        
    