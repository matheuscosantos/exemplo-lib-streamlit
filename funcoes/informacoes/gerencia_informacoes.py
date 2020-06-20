import streamlit as st
import pandas as pd


def exibe_numero_de_linhas(df):
    st.markdown('**Número de linhas:**')
    st.markdown(df.shape[0])


def exibe_numero_de_colunas(df):
    st.markdown('**Número de colunas:**')
    st.markdown(df.shape[1])


def exibe_amostra(df):
    st.markdown('**Visualizando o dataframe**')
    number = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
    st.dataframe(df.head(number))


def conta_tipo_de_dados(exploracao):
    st.markdown('**Contagem dos tipos de dados:**')
    st.write(exploracao.tipos.value_counts())


def exibe_nome_das_colunas_int64(exploracao):
    st.markdown('**Nomes das colunas do tipo int64:**')
    st.markdown(list(exploracao[exploracao['tipos'] == 'int64']['nomes']))


def exibe_nome_das_colunas_float64(exploracao):
    st.markdown('**Nomes das colunas do tipo float64:**')
    st.markdown(list(exploracao[exploracao['tipos'] == 'float64']['nomes']))


def exibe_nome_das_colunas_object64(exploracao):
    st.markdown('**Nomes das colunas do tipo object:**')
    st.markdown(list(exploracao[exploracao['tipos'] == 'object']['nomes']))


def exibe_nome_de_todas_colunas(df):
    st.markdown('**Nome das colunas:**')
    st.markdown(list(df.columns))

def consulta_colunas_e_tipos(df):
    aux = pd.DataFrame({"colunas": df.columns, "tipos": df.dtypes})
    return aux


def consulta_colunas_numericas(aux):
    colunas_numericas = list(aux[aux["tipos"] != "object"]["colunas"])
    return colunas_numericas


def consulta_colunas_objetos(aux):
    colunas_object = list(aux[aux["tipos"] == "object"]["colunas"])
    return  colunas_object


def consulta_colunas(df):
    colunas = list(df.columns)
    return colunas
