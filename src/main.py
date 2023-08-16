import os
import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk
from threading import Thread
from glob import glob
from database.connection import create_connection
from database.schema import create_tables
from config.create_folders import create_extraction_folders
from pdf_parser import parse_pdf
from database.queries import insert_transactions
import csv

# Definir caminho da pasta assets
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')

def read_pdf_files(folder_path):
    pdf_files = glob(os.path.join(folder_path, '*.pdf'))
    transactions = []

    for pdf_file in pdf_files:
        raw_transactions = parse_pdf(pdf_file)
        for transaction in raw_transactions:
            # Formatar o valor numérico removendo a vírgula e substituindo por ponto
            amount = transaction[2].replace(".", "").replace(",", ".")
            formatted_transaction = {
                "description": transaction[1],
                "date": transaction[0],
                "amount": amount,
                "transaction_type": transaction[3],
                "category": None,
                "subcategory": None
            }
            transactions.append(formatted_transaction)

    return transactions

def process_files():
    connection = create_connection()  # Conectar ao banco de dados

    create_tables(connection)  # Criar tabelas no banco de dados

    # Ler arquivos PDF da pasta selecionada
    selected_folder = folder_var.get()
    selected_folder_path = os.path.join(selected_folder, '')
    transactions = read_pdf_files(selected_folder_path)

    # Configurar a barra de progresso
    progress_bar['maximum'] = len(transactions)

    # Inserir as transações no banco de dados
    for idx, transaction in enumerate(transactions):
        insert_transactions(connection, [transaction])
        progress_bar['value'] = idx + 1
        percent_complete = (idx + 1) / len(transactions) * 100
        percent_label.config(text=f"{percent_complete:.1f}%")
        root.update()

    # Fechar a conexão com o banco de dados
    connection.close()

def generate_csv():
    connection = create_connection()  # Conectar ao banco de dados
    cursor = connection.cursor()

    transaction_type_filter = type_var.get()

    select_query = f"SELECT * FROM transactions WHERE transaction_type = '{transaction_type_filter}'"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    csv_filename = f"transactions_{transaction_type_filter}.csv"

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "description", "date", "amount", "transaction_type", "category", "subcategory"])
        writer.writerows(rows)

    cursor.close()
    connection.close()

    info_label.config(text=f"Arquivo '{csv_filename}' gerado com sucesso.")

def select_folder():
    selected_folder = filedialog.askdirectory(title="Selecione a pasta dos extratos")
    folder_var.set(selected_folder)

# Criação da janela da interface gráfica com estilo temático
root = ThemedTk(theme="arc")  # Escolha um tema que você goste
root.title("Processar Dados PDF")
root.geometry("500x250")  # Fixar tamanho da tela em 500x250

# Botão para selecionar a pasta dos extratos
folder_frame = ttk.Frame(root)
folder_frame.pack(fill=tk.X, padx=10, pady=10)
folder_var = tk.StringVar()
folder_var.set("")
folder_label = ttk.Label(folder_frame, text="Pasta dos Extratos:")
folder_label.pack(side=tk.LEFT)
folder_entry = ttk.Entry(folder_frame, textvariable=folder_var, state="readonly")
folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
select_button = ttk.Button(folder_frame, text="Selecionar", command=select_folder, style="Gray.TButton")
select_button.pack(side=tk.LEFT)

# Barra de progresso
progress_bar = ttk.Progressbar(root, mode='determinate', length=250)
progress_bar.pack(pady=(20, 0))

# Rótulo para exibir a porcentagem completa
percent_label = tk.Label(root, text="", font=("Helvetica", 12))
percent_label.pack()

# Botão para processar os dados com estilo moderno
process_button = ttk.Button(root, text="Processar Dados", command=process_files, style="Modern.TButton")
process_button.pack(pady=10)

# Criar um frame para os botões de filtro e gerar CSV
button_frame = ttk.Frame(root)
button_frame.pack()

# Dropdown para selecionar o tipo de transação
type_label = tk.Label(button_frame, text="Filtrar por Tipo:")
type_label.pack(side=tk.LEFT)
type_var = tk.StringVar()
type_var.set("C")
type_dropdown = ttk.Combobox(button_frame, textvariable=type_var, values=["C", "D"])
type_dropdown.pack(side=tk.LEFT)

# Botão para gerar o arquivo CSV
csv_button = ttk.Button(button_frame, text="Gerar CSV", command=generate_csv, style="Modern.TButton")
csv_button.pack(side=tk.LEFT, padx=5)

# Rótulo para exibir informações sobre o processo
info_label = ttk.Label(root, text="", font=("Helvetica", 12), foreground="#279EFF")
info_label.pack(pady=10)

root.mainloop()
