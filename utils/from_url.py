import re
def url_year(url):

    # Extract the year from the URL using regex
    year = re.search(r'/(\d{4})/', url)

    if year:
        return year.group(1)
    else:
        return "no year found in url"
