import openpyxl
import psycopg2
from utils.check import get_date, three_months, which_metric, get_multiplier
from utils.from_url import url_year
from pprint import pprint
from utils.check_document_name import year_from_name
from scraper.links_react import get_links_from_react_page
from scraper.ABB_scraper import get_excel_files
from scraper.links.excel import get_data_from_xlsx
import json
from datetime import datetime
from insert_into_postgres.insert import df_to_postgres

# Load company configuration
with open("config/config.json") as config_file:
    configs = json.load(config_file)

# Get data for each company
for company, config in configs.items():
    if config.get("skip") == False:
        print(f"Getting data for {company}...")
        links_xlsx = get_links_from_react_page(config)

        for link_xlsx in links_xlsx:

            url = link_xlsx['href']

            income_statements_dataframe = get_data_from_xlsx(url, company, config)

            df_to_postgres(income_statements_dataframe, 'income_statements', 'postgresql://postgres:OmxPassword@localhost:5432/postgres')
