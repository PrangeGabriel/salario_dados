import pandas as pd
import streamlit as st
from .database import get_connection

# Função para executar queries
@st.cache_data(ttl=600)  # Cache por 10 minutos
def run_query(query):
    conn = get_connection()
    return pd.read_sql(query, conn)

@st.cache_data(ttl=600)
def load_salarios_data():
    """Carrega todos os dados de salários"""
    return run_query("SELECT * FROM salarios")