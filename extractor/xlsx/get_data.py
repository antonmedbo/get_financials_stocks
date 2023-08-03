import pandas as pd
from pprint import pprint
from datetime import datetime
import json
from get_from_database.id_company_name import get_name_id

def from_sheet(company, index_quarters, index_metrics, workbook):

    # initialize dataframe
    financial_data = pd.DataFrame(columns=[
        "company_id", "date_range", "revenueproducts", "revenueservicesandother", 
        "totalrevenue", "costofgoodssold", "totalcostofgoodssold", "grossprofit", 
        "operatingexpenses", "rndexpenses", "otherexpenses", "operatingincome", 
        "nonoperatingincome", "interestandotherexpenses", "incomeafterfinancialitems", 
        "incometaxexpense", "incomenetoftax", "lossfromdiscontinuedoperations", 
        "netincome", "minorityinterestincome", "netattributableincome", "orderintake", 
        "adjustedgrossprofit", "adjustedebitda", "depreciation", "adjustedebita", 
        "investments"
    ])

    print(get_name_id(company))
    df = pd.read_excel(workbook, engine='openpyxl')

    for year, quarters in index_quarters.items():
        for quarter, index_quarter in quarters.items():
            row_data = {
                "company_id": get_name_id(company),
                "date_range": pd.to_datetime(f"{year}-{quarter[1:]}"),  # transform "Q4" to "4" and create date
            }

            for metric, index_metric in index_metrics.items():
                cell_value = df.iloc[index_metric, index_quarter]
                row_data[metric] = cell_value

            financial_data = pd.concat([financial_data, pd.DataFrame([row_data])], ignore_index=True)

    return financial_data