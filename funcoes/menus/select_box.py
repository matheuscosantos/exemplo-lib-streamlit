import streamlit as st

def menuPrincipal():
    opcao = st.selectbox(
        'Escolha a opção desejada',
        ('Estatística Descritiva Univariada', 'Amostras - São José dos Campos', 'Descrição dos dados')
    )
    return opcao


def menu_analise_das_colunas(df, colunas_numericas):
    col = st.selectbox('Selecione a coluna: ', colunas_numericas)
    if col is not None:
        st.markdown('Média')
        st.markdown(df[col].mean())

        st.markdown('Mediana')
        st.markdown(df[col].median())

        st.markdown('Desvio padrão')
        st.markdown(df[col].std())

        # st.markdown('Kurtosis')
        # st.markdown(df[col].kurtosis())
        #
        # st.markdown('Skewness')
        # st.markdown(df[col].skew())

        st.markdown('Describe')
        st.table(df[colunas_numericas].describe().transpose())
