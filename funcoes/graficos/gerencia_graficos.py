import altair as alt
import streamlit as st


def criar_histograma(coluna, df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
        alt.X(coluna, bin=True),
        y='count()', tooltip=[coluna, 'count()']
    ).interactive()
    return chart


def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width=600).mark_bar().encode(
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
        color=color,
        tooltip=[x, y]
    ).interactive()
    return scatter


def cria_correlationplot(df, colunas_numericas):
    cor_data = (df[colunas_numericas]).corr().stack().reset_index().rename(
        columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'})
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal
    base = alt.Chart(cor_data, width=500, height=500).encode(x='variable2:O', y='variable:O')
    text = base.mark_text().encode(text='correlation_label',
                                   color=alt.condition(alt.datum.correlation > 0.5,
                                                       alt.value('white'),
                                                       alt.value('black')))
    # The correlation heatmap itselfimport numpy as np

    cor_plot = base.mark_rect().encode(color='correlation:Q')

    return cor_plot + text


def cria_visualizacao_de_dados(df, colunas, colunas_numericas):
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
        col_num_x = st.selectbox('Selecione o valor de x ', colunas_numericas, key='unique')
        col_num_y = st.selectbox('Selecione o valor de y ', colunas_numericas, key='unique')
        col_color = st.selectbox('Selecione a coluna para cor', colunas)
        st.markdown('Selecione os valores de x e y')
        st.write(criar_scatterplot(col_num_x, col_num_y, col_color, df))

    correlacao = st.checkbox('Correlacao')
    if correlacao:
        st.markdown('Gráfico de correlação das colunas númericas')
        st.write(cria_correlationplot(df, colunas_numericas))


def gera_last_available_confirmed(df_sao_jose_dos_campos):
    st.subheader('Last available confirmed')
    df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_confirmed', figsize=(25, 10))
    return st.pyplot()


def last_available_confirmed_per_100k_inhabitants(df_sao_jose_dos_campos):
    st.subheader('Last available confirmed per 100k inhabitants')
    df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_confirmed_per_100k_inhabitants', figsize=(25, 10))
    return st.pyplot()


def new_confirmed(df_sao_jose_dos_campos):
    st.subheader('New confirmed')
    df_sao_jose_dos_campos.plot.bar(x='date', y='new_confirmed', figsize=(25, 10))
    return st.pyplot()


def last_available_deaths(df_sao_jose_dos_campos):
    st.subheader('Last available deaths')
    df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_deaths', figsize=(25, 10))
    return st.pyplot()


def new_deaths(df_sao_jose_dos_campos):
    st.subheader('New deaths')
    df_sao_jose_dos_campos.plot.bar(x='date', y='new_deaths', figsize=(25, 10))
    return st.pyplot()


def last_available_death_rate(df_sao_jose_dos_campos):
    st.subheader('Last available death rate')
    df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_death_rate', figsize=(25, 10))
    return st.pyplot()
