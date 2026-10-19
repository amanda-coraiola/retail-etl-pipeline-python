import pandas as pd
import numpy as np
import json
import logging
from datetime import datetime

# Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract_data():
    """Etapa 1: Extração de Dados Brutos Simulados (CSV e JSON)"""
    logging.info("Iniciando a etapa de Extração de Dados...")
    
    # Simulação de extração de transações brutas de vendas (CSV)
    raw_sales_data = {
        "transacao_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "data_hora": [
            "2026-10-15 10:15:00", "2026-10-15 11:30:00", "2026-10-15 12:45:00",
            "2026-10-16 09:20:00", "2026-10-16 14:10:00", "2026-10-16 16:50:00",
            "2026-10-17 10:00:00", "2026-10-17 18:05:00"
        ],
        "loja_id": [1, 2, 1, 3, 2, 1, 3, 2],
        "produto_id": [501, 502, 501, 503, 502, 504, 501, 503],
        "quantidade": [2, 1, 5, 1, 3, 10, 2, 4],
        "valor_unitario": [25.50, 120.00, 25.50, 45.00, 120.00, 15.00, 25.50, 45.00],
        "desconto": [0.0, 10.0, 5.0, 0.0, 15.0, 0.0, 0.0, 5.0]
    }
    
    # Simulação de dimensão de produtos (JSON)
    raw_products_data = [
        {"produto_id": 501, "nome_produto": "Shampoo Premium 400ml", "categoria": "Cabelos", "marca": "LuxeHair"},
        {"produto_id": 502, "nome_produto": "Kit Dermocosmético Anti-Idade", "categoria": "Skincare", "marca": "DermoCare"},
        {"produto_id": 503, "nome_produto": "Protetor Solar FPS 50", "categoria": "Skincare", "marca": "SunProtect"},
        {"produto_id": 504, "nome_produto": "Sabonete Hidratante 250ml", "categoria": "Corpo", "marca": "SoftSkin"}
    ]
    
    # Simulação de dimensão de lojas (CSV)
    raw_stores_data = {
        "loja_id": [1, 2, 3],
        "nome_loja": ["Loja Centro - SP", "Loja Shopping - RJ", "Loja E-commerce"],
        "regiao": ["Sudeste", "Sudeste", "Nacional"],
        "canal": ["Físico", "Físico", "Digital"]
    }
    
    df_sales = pd.DataFrame(raw_sales_data)
    df_products = pd.DataFrame(raw_products_data)
    df_stores = pd.DataFrame(raw_stores_data)
    
    logging.info("Extração concluída com sucesso.")
    return df_sales, df_products, df_stores

def transform_data(df_sales, df_products, df_stores):
    """Etapa 2: Transformação, Tratamento e Modelagem Dimensional Star Schema"""
    logging.info("Iniciando a etapa de Transformação e Modelagem Dimensional...")
    
    # Conversões e Tratamento de Datas
    df_sales["data_hora"] = pd.to_datetime(df_sales["data_hora"])
    
    # Construção da Dim_Tempo
    dim_tempo = pd.DataFrame({"data_hora": df_sales["data_hora"].unique()})
    dim_tempo["tempo_id"] = dim_tempo["data_hora"].dt.strftime("%Y%m%d%H%M")
    dim_tempo["data"] = dim_tempo["data_hora"].dt.date
    dim_tempo["ano"] = dim_tempo["data_hora"].dt.year
    dim_tempo["mes"] = dim_tempo["data_hora"].dt.month
    dim_tempo["dia"] = dim_tempo["data_hora"].dt.day
    dim_tempo["dia_semana"] = dim_tempo["data_hora"].dt.day_name()
    
    # Cálculo de métricas financeiras
    df_sales["valor_bruto"] = df_sales["quantidade"] * df_sales["valor_unitario"]
    df_sales["valor_liquido"] = df_sales["valor_bruto"] - df_sales["desconto"]
    
    # Mapeamento com chave de tempo
    df_sales["tempo_id"] = df_sales["data_hora"].dt.strftime("%Y%m%d%H%M")
    
    # Criação da Tabela Fato
    fato_vendas = df_sales[[
        "transacao_id", "tempo_id", "loja_id", "produto_id",
        "quantidade", "valor_unitario", "desconto", "valor_bruto", "valor_liquido"
    ]]
    
    dim_produtos = df_products.rename(columns={"produto_id": "produto_id"})
    dim_lojas = df_stores.rename(columns={"loja_id": "loja_id"})
    
    logging.info("Transformação realizada e modelo Star Schema gerado.")
    return fato_vendas, dim_produtos, dim_lojas, dim_tempo

def load_data(fato_vendas, dim_produtos, dim_lojas, dim_tempo):
    """Etapa 3: Carga dos Dados Processados (Simulação de Data Warehouse / CSV Target)"""
    logging.info("Iniciando a Carga de Dados no Data Warehouse...")
    
    fato_vendas.to_csv("fato_vendas.csv", index=False)
    dim_produtos.to_csv("dim_produtos.csv", index=False)
    dim_lojas.to_csv("dim_lojas.csv", index=False)
    dim_tempo.to_csv("dim_tempo.csv", index=False)
    
    logging.info("Carga concluída. Arquivos dimensionais gerados com sucesso!")

if __name__ == "__main__":
    logging.info("=== INICIANDO PIPELINE DE ETL ===")
    sales, products, stores = extract_data()
    fato, d_prod, d_loj, d_temp = transform_data(sales, products, stores)
    load_data(fato, d_prod, d_loj, d_temp)
    logging.info("=== PIPELINE FINALIZADO COM SUCESSO ===")
