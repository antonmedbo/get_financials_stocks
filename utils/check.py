from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_date(string, date_format="%b. %d, %Y"):
    try:
        datetime.strptime(string, date_format)
        return datetime.strptime(string, date_format)
    except ValueError:
        return False
    
def three_months(string):
    string = string.lower()
    try: 
        if "three" in string:
            return "three"
        elif "six" in string:
            return "six"
        else:
            return False
    except:
        return False

def which_metric(string):

    if "sales of products".lower() in string.lower():
        return "sales of products"
    if "Sales of services and other".lower() in string.lower():
        return "Sales of services and other"
    if "Total cost of sales".lower() in string.lower():
        return "Total cost of sales"
    if "Total revenues".lower() in string.lower():
        return "Total revenues"
    if "Cost of sales of products".lower() in string.lower():
        return "Cost of sales of products"
    if "Cost of services and other".lower() in string.lower():
        return "Cost of services and other"
    if "Gross profit".lower() in string.lower():
        return "Gross profit"
    if "Selling, general and administrative expenses".lower() in string.lower():
        return "Selling, general and administrative expenses"
    if "Non-order related research and development expenses".lower() in string.lower():
        return "Non-order related research and development expenses"
    if "Other income (expense), net".lower() in string.lower():
        return "Other income (expense), net"
    if "Income from operations".lower() in string.lower():
        return "Income from operations"
    if "Interest and dividend income".lower() in string.lower():
        return "Interest and dividend income"
    if "Interest and other finance expense".lower() in string.lower():
        return "Interest and other finance expense"
    if "Non-operational pension (cost) credit".lower() in string.lower():
        return "Non-operational pension (cost) credit"
    if "Income from continuing operations before taxes".lower() in string.lower():
        return "Income from continuing operations before taxes"
    if "Income tax expense".lower() in string.lower():
        return "Income tax expense"
    if "Income from continuing operations, net of tax".lower() in string.lower():
        return "Income from continuing operations, net of tax"
    if "Loss from discontinued operations, net of tax".lower() in string.lower():
        return "Loss from discontinued operations, net of tax"
    if "Net income".lower() in string.lower():
        return "Net income"
    if "Net income attributable to noncontrolling interests and ".lower() in string.lower():
        return "Net income attributable to noncontrolling interests and "
    if "redeemable noncontrolling interests".lower() in string.lower():
        return "redeemable noncontrolling interests"
    if "Net income attributable to ABB".lower() in string.lower():
        return "Net income attributable to ABB"
    if "Amounts attributable to ABB shareholders:".lower() in string.lower():
        return "Amounts attributable to ABB shareholders:"
    if "Income from continuing operations, net of tax".lower() in string.lower():
        return "Income from continuing operations, net of tax"
    if "Loss from discontinued operations, net of tax".lower() in string.lower():
        return "Loss from discontinued operations, net of tax"
    if "Net income".lower() in string.lower():
        return "Net income"
    if "Weighted-average number of shares outstanding (in millions) used to compute:".lower() in string.lower():
        return "Weighted-average number of shares outstanding (in millions) used to compute:"
    else:
        return
    
def get_multiplier(sheet):

    for row in sheet.iter_rows(values_only=True):
        for i in row:
            if isinstance(i, str):
                if "millions" in i.lower(): 
                    return 1000000
                else: 
                    continue