# -*- coding: utf-8 -*-
from pathlib import Path
import nbformat
from nbconvert import MarkdownExporter

# Caminho do arquivo
notebook_path = Path("/mnt/data/analise_de_dados_python.ipynb")

# Carregar o notebook
with notebook_path.open() as f:
    notebook = nbformat.read(f, as_version=4)

# Converter notebook para Markdown
exporter = MarkdownExporter()
body, resources = exporter.from_notebook_node(notebook)

# Exibir parte do conteúdo convertido para verificação
body[:1000]  # Mostrar os primeiros 1000 caracteres para revisão inicial




Original file is located at 
  https://colab.research.google.com/gist/ei-Gih/4b4df572e9745523710ca3a291193228/arquivo-inicial-minicurso-analise-de-dados-python.ipynb

# Desafio:

Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos enormes para a empresa

O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?

# O que temos:

Temos 1 base de dados com informações dos clientes, tanto clientes atuais quanto clientes que cancelaram o cartão

Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers


from google.colab import drive
drive.mount('/content/drive')

# **Logica do Programa**
- Passo 1: Importar a base de dados;
- Passo 2: Visualizar e tratar essa base de dados;
- Passo 3: Analisar a sua base de dados;
- Passo 4: Construir uma análise para identificar o motivo de cancelamento;
- Passo 5: Identificar qual o motivo ou os principais motivos dos clientes cancelarem o cartão;


import pandas as pd
tabela = pd.read_csv("/content/ClientesBanco.csv", encoding="latin1")
tabela= tabela.drop("CLIENTNUM", axis=1)
display(tabela)

## Agora vamos tratar valores vazios e exibir um resumo das colunas da base de dados"""

tabela= tabela.dropna()
display(tabela.info())

display(tabela.describe().round(1))

## Vamos avaliar como está a divisão entre Clientes x Cancelados"""

qtde_categoria = tabela["Categoria"].value_counts()
display(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
display(qtde_categoria_perc)

## Podemos olhar a comparação entre Clientes e Cancelados em cada uma das colunas da nossa base de dados, para ver se essa informações traz algum insight novo para a gente"""

import plotly.express as px

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()

# Iformações retiradas da análise

- Me parece que quanto mais produtos contratados um cliente tem, menor a chance dele cancelar.
- E quanto mais transações e quanto maior o valor de transações, menor a chance dele cancelar.
- Quanto maior a quantidade de contatos que a pessoa teve que fazer, maior a chance dela cancelar.
