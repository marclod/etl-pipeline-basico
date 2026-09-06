import requests
import pandas as pd
from datetime import datetime

def extrair_dados_fipe():
    
    print("Iniciando extração de dados da BrasilAPI...")
    url = "https://brasilapi.com.br/api/fipe/marcas/v1/carros"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados_json = resposta.json()
        print(f"Sucesso! {len(dados_json)} marcas encontradas.")
        
        print("Transformando os dados...")
        df = pd.DataFrame(dados_json)
        
        df['data_extracao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        df.columns = [coluna.lower() for coluna in df.columns]
        
        print("Salvando os dados...")
        nome_arquivo = "marcas_carros_fipe.csv"
        df.to_csv(nome_arquivo, index=False)
        
        print(f"Pipeline finalizado! Dados salvos no arquivo: {nome_arquivo}")
        
    else:
        print(f"Erro ao acessar a API. Código de status: {resposta.status_code}")

if __name__ == "__main__":
    extrair_dados_fipe()