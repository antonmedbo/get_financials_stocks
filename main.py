
from scraper.website import get_links
from scraper.excel import get_data_from_xlsx
import json
from insert_into_postgres.insert import df_to_postgres
from pprint import pprint

# Load company configuration
with open("config/config.json") as config_file:
    configs = json.load(config_file)

# Get data for each company
for company, config in configs.items():
    if config.get("skip") == False:
        print(f"Getting data for {company}...")
        
        links_xlsx = get_links(config)

        for link_xlsx in links_xlsx:

            url = link_xlsx['href']

            income_statements_dataframe = get_data_from_xlsx(url, company, config)

            break

            # df_to_postgres(income_statements_dataframe, 'income_statements', 'postgresql://postgres:OmxPassword@localhost:5432/postgres')
