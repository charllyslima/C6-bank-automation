import os

def create_extraction_folders():
    current_directory = os.path.dirname(__file__)
    assets_directory = os.path.join(current_directory, '..', 'assets')

    conta_corrente_folder = os.path.join(assets_directory, 'conta_corrente')
    cartao_credito_folder = os.path.join(assets_directory, 'cartao_credito')

    os.makedirs(conta_corrente_folder, exist_ok=True)
    os.makedirs(cartao_credito_folder, exist_ok=True)

    print("Pastas de extrato criadas com sucesso.")
