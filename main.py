import streamlit as st
import numpy as np

from funcoes.dados.gerencia_dados import csv_para_dataframe, gera_exploracao, filtra_dados_sao_jose_dos_campos, \
    gera_amostra
from funcoes.graficos.gerencia_graficos import *
from funcoes.informacoes.gerencia_informacoes import *
from funcoes.layout.componente import cria_cabecalho, cria_rodape
from funcoes.menus.select_box import menuPrincipal, menu_analise_das_colunas


def main():
    cria_cabecalho()
    exibe_fonte()
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

        st.markdown("## Amostra simples")
        st.markdown("#### Número de amostras: 4081")
        st.markdown("#### Grau de confiança: 99%")
        st.markdown("#### Margem de erro: 2%")

        amostra = df.sample(n=4081)

        amostra = amostra.drop(['index',
                                'epidemiological_week',
                                'city_ibge_code',
                                'estimated_population_2019',
                                'is_repeated',
                                'is_last',
                                'order_for_place',
                                'last_available_confirmed'], axis=1)


        aux = consulta_colunas_e_tipos(amostra)
        colunas_numericas = consulta_colunas_numericas(aux)
        colunas_object = consulta_colunas_objetos(aux)
        colunas = consulta_colunas(amostra)
        menu_analise_das_colunas(amostra, colunas_numericas)

        cria_visualizacao_de_dados(amostra, colunas, colunas_numericas, colunas_object)
        cria_rodape()
        #
        # aux_amostra = consulta_colunas_e_tipos(amostra)
        # colunas_numericas = consulta_colunas_numericas(aux_amostra)
        #
        # menu_analise_das_colunas(df, colunas_numericas)


    elif opcao == 'Amostras - São José dos Campos':

        df = filtra_dados_sao_jose_dos_campos(df)
        df = df.drop(['index',
                    'epidemiological_week',
                    'city_ibge_code',
                    'estimated_population_2019',
                    'is_repeated',
                    'is_last',
                    'order_for_place',
                    'last_available_confirmed'], axis=1)

        aux = consulta_colunas_e_tipos(df)
        colunas_numericas = consulta_colunas_numericas(aux)

        menu_analise_das_colunas(df, colunas_numericas)

        last_available_confirmed_per_100k_inhabitants(df)
        new_confirmed(df)
        last_available_deaths(df)
        new_deaths(df)
        last_available_death_rate(df)
        cria_rodape()

    elif opcao == 'Descrição dos dados':
        # st.markdown("* last_available_confirmed_per_100k_inhabitants:")
        # st.markdown("* Confirmados acum./100k hab. Número de casos confirmados por 100.000 habitantes do último dia disponível igual ou anterior à data date.")
        st.markdown("* last_available_confirmed_per_100k_inhabitants:"\
                    "   * Confirmados acum./100k hab. Número de casos confirmados por 100.000 habitantes do último dia disponível igual ou anterior à data date.")


if __name__ == '__main__':
    main()
