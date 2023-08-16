def insert_transactions(connection, transactions):
    try:
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO transactions (description, date, amount, category, subcategory, transaction_type)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        formatted_transactions = []

        for t in transactions:
            formatted_date = t["date"].strftime("%Y-%m-%d")  # Formatar a data para "YYYY-MM-DD"
            formatted_transactions.append((t["description"], formatted_date, t["amount"], t["category"], t["subcategory"], t["type"]))

        cursor.executemany(insert_query, formatted_transactions)
        connection.commit()

        print("Dados inseridos no banco de dados com sucesso!")

    except Exception as e:
        connection.rollback()
        print(f"Erro ao inserir dados no banco de dados: {e}")
    
    finally:
        cursor.close()
