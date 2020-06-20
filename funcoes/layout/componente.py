import streamlit as st


def cria_cabecalho():
    st.image('fatec.png', width=700)
    st.title('Projeto Final Estatística')
    st.header('Acompanhamento dos últimos 3 meses do COVID-19')


def cria_rodape():
    st.subheader('')
    st.subheader('Elaborado por ARIANA R. CURSINO e MATHEUS DA C. O. SANTOS - 4º ADS B')