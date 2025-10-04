# 3_src/database.py
import streamlit as st
import psycopg

# Configuração da conexão
@st.cache_resource
def init_connection():
    return psycopg.connect(
        host=st.secrets["DB_HOST"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        port=st.secrets["POSTGRES_PORT"]
    )

def get_connection():
    return init_connection()