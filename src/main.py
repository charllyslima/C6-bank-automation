import os
from glob import glob
from datetime import datetime
from database.connection import create_connection
from database.schema import create_tables
from config.create_folders import create_extraction_folders
from pdf_parser import parse_pdf
from database.queries import insert_transactions

# Definir caminho da pasta assets
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

def read_pdf_files(folder_path):
    pdf_files = glob(os.path.join(folder_path, '*.pdf'))
    transactions = []

    for pdf_file in pdf_files:
        raw_transactions = parse_pdf(pdf_file)
        print(raw_transactions)
        for transaction in raw_transactions:
             # Formatar o valor numérico removendo a vírgula e substituindo por ponto
            amount = transaction[2].replace(".", "").replace(",", ".")
            formatted_transaction = {
                "description": transaction[1],
                "date": transaction[0],
                "amount": amount,
                "type": transaction[3],
                "category": None,
                "subcategory": None
            }
            transactions.append(formatted_transaction)

    return transactions

def main():
    create_extraction_folders()  # Criar pastas de extrato

    connection = create_connection()  # Conectar ao banco de dados

    create_tables(connection)  # Criar tabelas no banco de dados

    # Ler arquivos PDF da pasta conta_corrente
    conta_corrente_folder = os.path.join(ASSETS_PATH, 'conta_corrente')
    conta_corrente_transactions = read_pdf_files(conta_corrente_folder)

    # Ler arquivos PDF da pasta conta_credito
    conta_credito_folder = os.path.join(ASSETS_PATH, 'conta_credito')
    conta_credito_transactions = read_pdf_files(conta_credito_folder)

    # Combina as transações das duas fontes
    all_transactions = conta_corrente_transactions + conta_credito_transactions
    # Inserir as transações no banco de dados
    insert_transactions(connection, all_transactions)

    # Fechar a conexão com o banco de dados
    connection.close()


if __name__ == "__main__":
    main()
