import os
import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def extrair_dados_fipe():
    print("Iniciando extração...")
    url = "https://brasilapi.com.br/api/fipe/marcas/v1/carros"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados_json = resposta.json()
        
        print("Transformando os dados...")
        df = pd.DataFrame(dados_json)
        df['data_extracao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.columns = [coluna.lower() for coluna in df.columns]
        
        print("Conectando ao PostgreSQL de forma segura...")
        
        usuario = os.getenv("DB_USER")
        senha = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST")
        banco = os.getenv("DB_NAME")
        
        engine = create_engine(f"postgresql://{usuario}:{senha}@{host}:5432/{banco}")
        
        df.to_sql("marcas_carros", engine, if_exists="replace", index=False)
        print("Pipeline finalizado! Dados salvos com segurança.")
        
    else:
        print("Erro na API.")

if __name__ == "__main__":
    extrair_dados_fipe()