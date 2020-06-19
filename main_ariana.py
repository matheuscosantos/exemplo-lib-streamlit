import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import base64

def criar_histograma(coluna, df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
        alt.X(coluna, bin=True),
        y='count()', tooltip=[coluna, 'count()']
    ).interactive()
    return chart

def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width = 600).mark_bar().encode(
        x=alt.X(coluna_num, stack='zero'),
        y=alt.Y(coluna_cat),
        tooltip=[coluna_cat, coluna_num]
    ).interactive()
    return bars

def criar_boxplot(coluna_num, coluna_cat, df):
    boxplot = alt.Chart(df, width=600).mark_boxplot().encode(
        x=coluna_num,
        y=coluna_cat
    )
    return boxplot

def criar_scatterplot(x, y, color, df):
    scatter = alt.Chart(df, width=800, height=400).mark_circle().encode(
        alt.X(x),
        alt.Y(y),
        color = color,
        tooltip = [x, y]
    ).interactive()
    return scatter

def cria_correlationplot(df, colunas_numericas):
    cor_data = (df[colunas_numericas]).corr().stack().reset_index().rename(columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'})
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal
    base = alt.Chart(cor_data, width=500, height=500).encode( x = 'variable2:O', y = 'variable:O')
    text = base.mark_text().encode(text = 'correlation_label',color = alt.condition(alt.datum.correlation > 0.5,alt.value('white'),
    alt.value('black')))
# The correlation heatmap itself
    cor_plot = base.mark_rect().encode(
    color = 'correlation:Q')

    return cor_plot + text

def main():
    st.image('fatec.png', width= 700)
    st.title('Projeto Final Estatística')
    st.header('Acompanhamento dos últimos 3 meses do COVID-19')
    st.subheader('Estatística Descritiva Univariada')
    df = pd.read_csv("dados/covid19_amostra.csv", sep=',')
    df.reset_index(inplace=True)
    df.dropna(inplace=True)

    st.markdown('**Número de linhas:**')
    st.markdown(df.shape[0])

    st.markdown('**Número de colunas:**')
    st.markdown(df.shape[1])

    st.markdown('**Visualizando o dataframe**')
    number = st.slider('Escolha o numero de colunas que deseja ver', min_value=1, max_value=20)
    st.dataframe(df.head(number))

    exploracao = pd.DataFrame({'nomes' : df.columns, 'tipos' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
    st.markdown('**Contagem dos tipos de dados:**')
    st.write(exploracao.tipos.value_counts())
    st.markdown('**Nomes das colunas do tipo int64:**')
    st.markdown(list(exploracao[exploracao['tipos'] == 'int64']['nomes']))
    st.markdown('**Nomes das colunas do tipo float64:**')
    st.markdown(list(exploracao[exploracao['tipos'] == 'float64']['nomes']))
    st.markdown('**Nomes das colunas do tipo object:**')
    st.markdown(list(exploracao[exploracao['tipos'] == 'object']['nomes']))   
    st.markdown('**Nome das colunas:**')
    st.markdown(list(df.columns))

    aux = pd.DataFrame({"colunas": df.columns, "tipos": df.dtypes})
    colunas_numericas = list(aux[aux["tipos"] != "object"]["colunas"])
    colunas_object = list(aux[aux["tipos"] == "object"]["colunas"])
    colunas = list(df.columns)
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

    st.subheader('Visualização dos Dados')
    st.image('https://i.kym-cdn.com/photos/images/original/001/333/670/35c.gif', width=200)
    st.markdown('Selecione a Visualização')

    histograma = st.checkbox('Histograma')
    if histograma:
        col_num = st.selectbox('Selecione a Coluna Numérica: ', colunas_numericas)
        st.markdown('Histograma da coluna: ' + str(col_num))
        st.write(criar_histograma(col_num, df))
    
    barras = st.checkbox('Gráfico de Barras')
    if barras:
        col_num_barras = st.selectbox('Selecione a Coluna numérica: ', colunas_numericas)
        col_cat_barras = st.selectbox('Selecione uma Coluna categórica: ', colunas_object)
        st.markdown('Gráfico de barras da coluna ' + str(col_cat_barras + ' pela coluna ' + col_num_barras))
        st.write(criar_barras(col_num_barras, col_cat_barras, df))

    boxplot = st.checkbox('Boxplot')
    if boxplot:
        col_num_box = st.selectbox('Selecione a Coluna numérica: ', colunas_numericas)
        col_cat_box = st.selectbox('Selecione uma Coluna categórica: ', colunas_object)    
        st.markdown('Boxplot ' + str(col_cat_box) + ' pela coluna ' + col_num_box)          
        st.write(criar_boxplot(col_num_box, col_cat_box, df)) 

    scatter = st.checkbox('Scatterplot')
    if scatter:
        col_num_x = st.selectbox('Selecione o valor de x ', colunas_numericas, key = 'unique')
        col_num_y = st.selectbox('Selecione o valor de y ', colunas_numericas, key = 'unique')
        col_color = st.selectbox('Selecione a coluna para cor', colunas)
        st.markdown('Selecione os valores de x e y')
        st.write(criar_scatterplot(col_num_x, col_num_y, col_color, df))

    correlacao = st.checkbox('Correlacao')
    if correlacao:
        st.markdown('Gráfico de correlação das colunas númericas')
        st.write(cria_correlationplot(df, colunas_numericas))    
        
    if scatter:
        col_num_x = st.selectbox('Selecione o valor de x ', colunas_numericas, key = 'unique')
        col_num_y = st.selectbox('Selecione o valor de y ', colunas_numericas, key = 'unique')
        col_color = st.selectbox('Selecione a coluna para cor', colunas)
        st.markdown('Selecione os valores de x e y')
        st.write(criar_scatterplot(col_num_x, col_num_y, col_color, df))   

    st.subheader('')
    st.subheader('Elaborado por ARIANA R. CURSINO e MATHEUS DA C. O. SANTOS - 4º ADS B')
        

if __name__ == '__main__':
    main()

