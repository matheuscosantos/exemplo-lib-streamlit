import streamlit as st
import numpy as np

from funcoes.dados.gerencia_dados import csv_para_dataframe, gera_exploracao, filtra_dados_sao_jose_dos_campos
from funcoes.graficos.gerencia_graficos import *
from funcoes.informacoes.gerencia_informacoes import *
from funcoes.layout.componente import cria_cabecalho, cria_rodape
from funcoes.menus.select_box import menuPrincipal, menu_analise_das_colunas


def main():
    cria_cabecalho()
    df = csv_para_dataframe()
    opcao = menuPrincipal()

    if opcao == 'Estatística Descritiva Univariada':
        exibe_numero_de_linhas(df)
        exibe_numero_de_colunas(df)
        exibe_amostra(df)
        exploracao = gera_exploracao(df)
        conta_tipo_de_dados(exploracao)
        exibe_nome_das_colunas_int64(exploracao)
        exibe_nome_das_colunas_float64(exploracao)
        exibe_nome_das_colunas_object64(exploracao)
        exibe_nome_de_todas_colunas(df)

        aux = consulta_colunas_e_tipos(df)
        colunas_numericas = consulta_colunas_numericas(aux)
        colunas_object = consulta_colunas_objetos(aux)
        colunas = consulta_colunas(df)
        menu_analise_das_colunas(df, colunas_numericas)

        cria_visualizacao_de_dados(df, colunas, colunas_numericas)
        cria_rodape()

    elif opcao == 'Amostras - São José dos Campos':
        df = filtra_dados_sao_jose_dos_campos(df)
        gera_last_available_confirmed(df)
        last_available_confirmed_per_100k_inhabitants(df)
        new_confirmed(df)
        last_available_deaths(df)
        new_deaths(df)
        last_available_death_rate(df)
        cria_rodape()


if __name__ == '__main__':
    main()
