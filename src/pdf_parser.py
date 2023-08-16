import os
from PyPDF2 import PdfReader
from datetime import datetime

def parse_pdf(file_path):
    transactions = []

    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            lines = text.split('\n')

            for line in lines:
                parts = line.split(' ')

                if len(parts) >= 5:
                    date_str = parts[0]
                    description = ' '.join(parts[1:-2])
                    amount = parts[-2]
                    transaction_type = parts[-1]

                    try:
                        date = datetime.strptime(date_str, '%d/%m/%Y')
                        
                        # Ignorar linhas com descrições contendo "SALDO" ou "TOTAL DISPONÍVEL PARA SAQUE"
                        if not (description.startswith(' -    ') or "SALDO" in description or "TOTAL DISPONÍVEL PARA SAQUE" in description):
                            # Remover "000000000000" da descrição
                            description = description.replace('000000000000', '').strip()
                            # Substituir "-" por " - "
                            description = description.replace('-', ' - ')

                            transactions.append([date, description, amount, transaction_type])
                            print(f"Data: {date}, Descrição: {description}, Valor: {amount}, Tipo: {transaction_type}")
                    except ValueError:
                        # Ignorar linhas com data inválida
                        pass

    return transactions
