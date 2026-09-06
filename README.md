# 🚗 Pipeline ETL: Extração de Dados da Tabela FIPE (BrasilAPI)

Este repositório documenta o meu processo de aprendizado na construção de pipelines de dados (ETL - Extract, Transform, Load) utilizando Python. 

Para demonstrar a minha evolução técnica, dividi este projeto em duas abordagens, começando da extração mais simples até a integração com um banco de dados relacional.

## 🎯 Objetivo
Consumir dados de uma API pública (BrasilAPI), realizar o tratamento dos dados utilizando a biblioteca Pandas e carregar essas informações em diferentes destinos, evidenciando o entendimento do fluxo de dados.

## 📖 A Evolução do Projeto (Meus Aprendizados)

O projeto foi construído em duas etapas, representadas por dois scripts distintos:

### Fase 1: O Script Básico (Extração para CSV)
* **Arquivo:** `etl_fipeCSV.py`
* **O que faz:** Faz a requisição na API utilizando `requests`, formata o JSON recebido em um DataFrame do `pandas`, adiciona uma coluna de auditoria (`data_extracao`) e salva o resultado final em um arquivo local `.csv`.
* **Aprendizados:** Compreensão do ciclo de requisições HTTP, manipulação básica de DataFrames, padronização de colunas e uso do bloco `if __name__ == "__main__"` para modularização do código.

### Fase 2: O Script Avançado (Carga no Banco de Dados)
* **Arquivo:** `etl_fipeBD.py`
* **O que faz:** Realiza a mesma extração e transformação da Fase 1, mas substitui a geração do arquivo local pela conexão e inserção direta dos dados em um banco **PostgreSQL**.
* **Aprendizados:** Configuração e uso do banco de dados relacional PostgreSQL, utilização da biblioteca `SQLAlchemy` como engine de conexão e implementação de segurança através do `python-dotenv` para ocultar credenciais (`.env`).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas Principais:** `pandas`, `requests`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv`
* **Banco de Dados:** PostgreSQL

## 🚀 Como executar este projeto
1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente e instale as dependências: `pip install pandas requests psycopg2-binary sqlalchemy python-dotenv`
4. Para a Fase 1: Rode `python etl_fipeCSV.py` e verifique o arquivo `.csv` gerado.
5. Para a Fase 2: 
   * Crie um banco de dados no seu PostgreSQL local.
   * Crie um arquivo `.env` na raiz do projeto contendo suas credenciais (DB_USER, DB_PASS, DB_HOST, DB_NAME).
   * Rode `python etl_fipeBD.py` e verifique a tabela criada no seu banco.