import pandas as pd
from pprint import pprint
from datetime import datetime
import json

def from_sheet(index_quarters, workbook):

    df = pd.read_excel(workbook, engine='openpyxl')
    json_data = {}
    for index, row in df.iterrows():
        
        for year, quarters in index_quarters.items():
            json_data[year] = {}
            for quarter, position in quarters.items():
                
                if quarter not in json_data[year]:
                    json_data[year][quarter] = {}
                    
                if row[position] and row[0]:
                    
                    json_data[year][quarter].update({row[0]:row[position]})

    with open('data.json', 'w') as f:
        json.dump(json_data, f, indent=4)
    return json_data



