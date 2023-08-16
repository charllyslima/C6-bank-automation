# Automação de Dados Bancários

Este projeto consiste em uma aplicação de automação para processar extratos bancários em formato PDF e armazenar as informações relevantes em um banco de dados. Além disso, permite gerar arquivos CSV filtrados por tipo de transação.

![image](https://github.com/charllyslima/C6_Bank_Automation/assets/96506145/5db25526-6608-4c32-8113-edb57cee8a43)

## Requisitos

Certifique-se de ter o Python 3.8 ou superior instalado em seu sistema.

## Instalação

1. Clone este repositório para o seu computador:

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

No Windows:

```bash
venv\Scripts\activate
```

No macOS e Linux:

```bash
source venv/bin/activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

1. Execute o aplicativo com o seguinte comando:

```bash
python main.py
```

2. A interface gráfica será exibida, permitindo que você selecione a pasta dos extratos bancários. Clique no botão "Selecionar" para escolher a pasta que contém os arquivos PDF dos extratos.

3. Depois de selecionar a pasta, clique no botão "Processar Dados" para processar os extratos e armazenar as informações no banco de dados. A barra de progresso exibirá o progresso do processamento.

4. Use o menu suspenso "Filtrar por Tipo" para selecionar o tipo de transação (C - Crédito ou D - Débito) que deseja incluir no arquivo CSV.

5. Clique no botão "Gerar CSV" para gerar um arquivo CSV filtrado de acordo com o tipo de transação selecionado. O arquivo será gerado na mesma pasta do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação de pull.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

