# 🏗️ Retail Data Warehouse - ETL Pipeline & Dimensional Modeling

> Pipeline automatizado em Python para extração, limpeza, transformação e carga (ETL) de dados brutos de transações de varejo em uma modelagem dimensional (*Star Schema*).

---

## 🎯 Sobre o Projeto
Este repositório demonstra a construção de um pipeline de **Engenharia de Dados** completo para o ecossistema de varejo. O script extrai dados de fontes heterogêneas (vendas, cadastro de produtos e lojas), realiza tratamentos de qualidade de dados, aplica regras de negócio e estrutura um modelo dimensional composto por uma **Tabela Fato** e três **Tabelas Dimensão**.

---

## 🏛️ Arquitetura do Modelo Dimensional (Star Schema)

   +------------------+
   |   Dim_Produtos   |
   +------------------+
             |
             | (1:N)
             v
+------------+  (1:N)  +------------------+  (N:1)  +------------------+
| Dim_Tempo  |-------->|   Fato_Vendas    |<--------|    Dim_Lojas     |
+------------+         +------------------+         +------------------+


### 📋 Detalhamento das Tabelas:
* **`Fato_Vendas`**: Registra as métricas quantitativas e financeiras de cada transação (`quantidade`, `valor_bruto`, `desconto`, `valor_liquido`).
* **`Dim_Produtos`**: Atributos descritivos do catálogo de produtos (`categoria`, `marca`, `nome_produto`).
* **`Dim_Lojas`**: Informações geográficas e de canais de vendas (`regiao`, `canal`, `nome_loja`).
* **`Dim_Tempo`**: Granularidade temporal detalhada (`ano`, `mes`, `dia`, `dia_semana`).

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**: Linguagem principal para orquestração da lógica de ETL.
* **Pandas**: Manipulação de DataFrames, tratamento de datas e agregações.
* **Logging**: Monitoramento e auditoria em tempo real das etapas de execução do pipeline.

---

## 🚀 Como Executar o Pipeline Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/amanda-coraiola/retail-etl-pipeline-python.git](https
