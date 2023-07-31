import io
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from extractor.get_data import from_excel


list_income_statements = []
response = requests.get("https://global.abb/group/en/investors/quarterly-results")
soup = BeautifulSoup(response.content, 'html.parser')

# Fetch all the links that contain 'XLSX' in their text
links = soup.find_all('a', text=lambda text: text and "xlsx" in text.lower())

for link in links:
    url = link['href']

    # Some links might be relative, so we need to make them absolute
    if url.startswith("/"):
        url = "https://global.abb.com" + url

    
    
    
    # # Get the content of the excel file
    # response = requests.get(url)
    # content = response.content

    # file_name = url.split("/")[-1]

    # # Load the workbook into memory
    # workbook = load_workbook(filename=io.BytesIO(content))

    # # For example, print out the values of the first sheet
    # sheet = workbook.active

    # income_statement = from_excel(sheet, file_name)

    # list_income_statements.append(income_statement)

