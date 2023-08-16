# Projeto de Importação de Dados do C6 Bank

Este projeto tem como objetivo importar dados de extratos em formato PDF do C6 Bank, interpretá-los e salvar as transações em um banco de dados MySQL.

![image](https://github.com/charllyslima/C6_Bank_Automation/assets/96506145/5db25526-6608-4c32-8113-edb57cee8a43)


## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.7 ou superior
- MySQL Server

## Instalação

1. Clone o repositório para o seu sistema local:

```bash
git clone https://github.com/charllyslima/C6_Bank_Automation.git
```

2. Navegue até o diretório do projeto:

```bash
cd C6_Bank_Automation
```

3. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
```

4. Ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

5. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

6. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente:

```
MYSQL_HOST=seu-host
MYSQL_USER=seu-usuario
MYSQL_PASSWORD=sua-senha
MYSQL_DB=seu-banco
```

7. Execute o script principal:

```bash
python main.py
```

## Utilização

- Ao executar o script `main.py`, a interface gráfica será aberta.
- Clique no botão "Processar Dados" para importar e processar os extratos PDF.
- A barra de progresso mostrará o progresso do processamento.
- Após o processamento, os dados serão inseridos no banco de dados MySQL.

![image](https://github.com/charllyslima/C6_Bank_Automation/assets/96506145/39467719-03c6-44cf-989a-28d696db9603)
![image](https://github.com/charllyslima/C6_Bank_Automation/assets/96506145/d534c219-4f23-48de-b74d-304e01ca900d)


## Gerar CSV

- Para gerar um arquivo CSV com as transações filtradas pelo tipo, insira o tipo desejado (C ou D) no campo "Filtrar por Tipo".
- Clique no botão "Gerar CSV" para criar o arquivo CSV com as transações filtradas.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
```

Lembre-se de substituir `seu-usuario`, `nome-do-repositorio`, `seu-host`, `seu-usuario`, `sua-senha` e `seu-banco` pelas informações corretas para o seu ambiente.
