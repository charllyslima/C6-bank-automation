def create_tables(connection):
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id SERIAL PRIMARY KEY,
        description TEXT,
        date DATE NOT NULL,
        amount DECIMAL(10, 2),
        category TEXT,
        subcategory TEXT,
        transaction_type VARCHAR(1)
    )
    """

    cursor.execute(create_table_query)
    connection.commit()

    cursor.close()
