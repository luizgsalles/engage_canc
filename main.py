import pandas as pd
import numpy as np
import warnings
import os
import datetime as dt
import streamlit as st

warnings.simplefilter("ignore", UserWarning)

# Configurar a página
st.set_page_config(layout="wide")

# Função para carregar os dados
@st.cache_resource
def load_data():
    return pd.read_excel('db_2024-07-30_11h48.xlsx')

# Função para salvar os dados
def save_data(df):
    df.to_excel('db_2024-07-29_15h48.xlsx_atualizado.csv', index=False)

# Carregar os dados
df = load_data()

# Centralizar o título do aplicativo
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Dashboard de Auditoria de Pedidos</h1>", unsafe_allow_html=True)

# Menu lateral para filtros
st.sidebar.title('Filtros')

# Exemplo de filtro para uma coluna específica
coluna_filtro_1 = st.sidebar.selectbox('Selecione a Coluna para Filtrar', df.columns)
valores_filtro_1 = st.sidebar.multiselect(f'Selecione os Valores para {coluna_filtro_1}', df[coluna_filtro_1].unique())

# Aplicar o filtro
if valores_filtro_1:
    df = df[df[coluna_filtro_1].isin(valores_filtro_1)]

# Adicionar CSS para ajustar a largura da tabela
st.markdown(
    """
    <style>
    .reportview-container .dataframe {
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir os dados em uma tabela interativa com tamanho ajustado
st.dataframe(df, height=600)
