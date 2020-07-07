import streamlit as st

def menuPrincipal():
    opcao = st.selectbox(
        'Escolha a opção desejada',
        ('Estatística Descritiva Univariada', 'Amostras - São José dos Campos')
    )
    return opcao


def menu_analise_das_colunas(df, colunas_numericas):
    col = st.selectbox('Selecione a coluna: ', colunas_numericas)
    if col is not None:
        st.markdown('Selecione o que deseja analisar: ')

        mean = st.checkbox('Média')
        if mean:
            st.markdown(df[col].mean())

        median = st.checkbox('Mediana')
        if median:
            st.markdown(df[col].median())

        desvio_pad = st.checkbox('Desvio padrão')
        if desvio_pad:
            st.markdown(df[col].std())

        kurtosis = st.checkbox('Kurtosis')
        if kurtosis:
            st.markdown(df[col].kurtosis())

        skewness = st.checkbox('Skewness')
        if skewness:
            st.markdown(df[col].skew())

        describe = st.checkbox('Describe')
        if describe:
            st.table(df[colunas_numericas].describe().transpose())
