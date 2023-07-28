import io
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from zipfile import BadZipFile
from extracter.get_data import from_excel

def get_excel_files_ABB():
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

        # Get the parent tr of the a element
        parent_tr = link.find_parent('tr')

        # Get the text of the first td in the parent tr, and extract the year
        year = parent_tr.find('td').get_text(strip=True).split(' ')[1]

        print(url)

        # Get the content of the excel file
        response = requests.get(url)
        content = response.content


        try:
            # Load the workbook into memory
            workbook = load_workbook(filename=io.BytesIO(content))

            # For example, print out the values of the first sheet
            sheet = workbook.active

            income_statement = from_excel(sheet, year)

            list_income_statements.append(income_statement)
        except BadZipFile:
            print(f"Invalid or corrupted file: {url}")
    
    return list_income_statements

