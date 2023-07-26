import re

def year_from_name(doc_name):

    # This regular expression looks for four consecutive digits followed by a hyphen or an underscore
    regex = r"\d{4}(?=[-_])"

    # Use the search method to find the year
    year_match = re.search(regex, doc_name)


    # Check if the search was successful
    if year_match:
        # Get the year
        year = year_match.group(0)
        return(year)
    else:
        print("ERROR: Year not found in document name.")


