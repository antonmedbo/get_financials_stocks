from sqlalchemy import create_engine, MetaData, Table, select

def get_name_id(company): 
    # Create an engine that connects to PostgreSQL
    engine = create_engine('postgresql://postgres:OmxPassword@localhost:5432/postgres')

    # Initialize metadata
    metadata = MetaData()

    # Load 'companies' table
    companies = Table('companies', metadata, autoload_with=engine)

    # Create a select query
    stmt = select(companies.columns.id).where(companies.columns.name == company)

    # Execute the query
    with engine.connect() as connection:
        result = connection.execute(stmt)

    # Get the company id
    company_id = result.scalar()

    return company_id
