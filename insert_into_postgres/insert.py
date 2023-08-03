from sqlalchemy import create_engine

def df_to_postgres(df, table_name, db_connection):
    """
    Insert pandas DataFrame into PostgreSQL table.

    :param df: DataFrame to insert
    :param table_name: PostgreSQL table name
    :param db_connection: Database connection string
    """
    engine = create_engine(db_connection)

    # Assuming DataFrame column names match the database table column names
    df.to_sql(table_name, engine, if_exists='append', index=False)

