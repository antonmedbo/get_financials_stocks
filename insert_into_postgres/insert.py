import psycopg2
import psycopg2.extras
from datetime import datetime
import json

def get_company_id(cur, company_name):
    select_query = "SELECT id FROM companies WHERE name = %s"
    cur.execute(select_query, (company_name,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        print(f"No company found with name: {company_name}")
        return None

def parse_data(data, company_id):
    # Check for empty date strings and skip the entry if found
    if not data["start_date"] or not data["end_date"]:
        return None

    # start_date = datetime.strptime(data["start_date"], '%Y-%m-%dT%H:%M:%S').date()
    # end_date = datetime.strptime(data["end_date"], '%Y-%m-%dT%H:%M:%S').date()
    # date_range = f"[{start_date}, {end_date}]"

    date_range = f"[{data['start_date']}, {data['end_date']}]"

    # Return the values as a tuple
    return (
        company_id,
        date_range,
        data.get("sales of products"),
        data.get("Sales of services and other"),
        data.get("Total revenues"),
        data.get("Cost of services and other"),
        data.get("Total cost of sales"),
        data.get("Gross profit"),
        data.get("Selling, general and administrative expenses"),
        data.get("Non-order related research and development expenses"),
        data.get("Other income (expense), net"),
        data.get("Income from operations"),
        data.get("Interest and dividend income"),
        data.get("Interest and other finance expense"),
        data.get("Non-operational pension (cost) credit"),
        data.get("Income from continuing operations before taxes"),
        data.get("Income tax expense"),
        data.get("Income from continuing operations, net of tax"),
        data.get("Loss from discontinued operations, net of tax"),
        data.get("Net income"),
    )




def add_financial_statement(data):
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='OmxPassword',
            host='localhost',
            port='5432'
        )
        # Create a new cursor
        cur = connection.cursor()

        company_id = get_company_id(cur, 'ABB Ltd')

        # # Get the data
        # with open('data.json') as f:
        #     data = json.load(f)

        data_tuples = [parse_data(d, company_id) for d in data]
        data_tuples = [dt for dt in data_tuples if dt is not None]

        insert_query = f'''
            INSERT INTO financial_data (
                company_id,
                date_range,
                sales_of_products,
                sales_of_services_and_other,
                total_revenues,
                cost_of_services_and_other,
                total_cost_of_sales,
                gross_profit,
                selling_general_and_admin_expenses,
                non_order_related_research_and_development_expenses,
                other_income_expense_net,
                income_from_operations,
                interest_and_dividend_income,
                interest_and_other_finance_expense,
                non_operational_pension_cost_credit,
                income_from_continuing_operations_before_taxes,
                income_tax_expense,
                income_from_continuing_operations_net_of_tax,
                loss_from_discontinued_operations_net_of_tax,
                net_income
            ) VALUES %s
        '''

        psycopg2.extras.execute_values(
            cur,
            insert_query,
            data_tuples,
            page_size=500
        )

        connection.commit()

    except Exception as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Close the cursor and the connection
        if cur:
            cur.close()
        if connection:
            connection.close()


