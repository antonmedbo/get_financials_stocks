import io
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from extracter.get_data import from_excel

# Get the webpage

def get_excel_files_ABB():
    response = requests.get("https://global.abb/group/en/investors/quarterly-results")
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the excel file links
    links = soup.select("a[href$='.xlsx']")

    # Loop through all links
    for link in links:
        url = link['href']

        # Some links might be relative, so we need to make them absolute
        if url.startswith("/"):
            url = "https://global.abb.com" + url

        # Get the content of the excel file
        response = requests.get(url)
        content = response.content

        file_name = url.split("/")[-1]

        # Load the workbook into memory
        workbook = load_workbook(filename=io.BytesIO(content))

        # For example, print out the values of the first sheet
        sheet = workbook.active
        from_excel(sheet, file_name)