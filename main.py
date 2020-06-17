import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

df = pd.read_csv("dados/covid19.csv", sep=',')
df.reset_index(inplace=True)
df.dropna(inplace=True)

amostra = df.head(3)

st.write(amostra)

df['city_ibge_code'] =  df['city_ibge_code'].astype(np.int64)
df['date'] =pd.to_datetime(df.date)

# tipo_de_dados = df.info()

st.write(df.last_available_confirmed_per_100k_inhabitants.median())

st.write(df.last_available_confirmed_per_100k_inhabitants.mode())

st.write(df.last_available_confirmed_per_100k_inhabitants.quantile())

st.write(df.last_available_confirmed_per_100k_inhabitants.var())

st.write(df.last_available_confirmed_per_100k_inhabitants.mad())

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df_only_numerics = df.select_dtypes(include=numerics)
new_df_only_numerics = df_only_numerics.drop(columns=['index','epidemiological_week','order_for_place','city_ibge_code'])
st.dataframe(new_df_only_numerics.cov())

st.dataframe(new_df_only_numerics.corr())

st.dataframe(new_df_only_numerics.skew())

df_sao_jose_dos_campos = df[df.city_ibge_code.eq(3549904)]
df_sao_jose_dos_campos.sort_values('date', ascending=True, inplace=True)

df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_confirmed', figsize=(25,10))
st.pyplot()
df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_confirmed_per_100k_inhabitants', figsize=(25,10))
st.pyplot()
df_sao_jose_dos_campos.plot.bar(x='date', y='new_confirmed', figsize=(25,10))
st.pyplot()
df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_deaths', figsize=(25,10))
st.pyplot()
df_sao_jose_dos_campos.plot.bar(x='date', y='new_deaths', figsize=(25,10))
st.pyplot()
df_sao_jose_dos_campos.plot.bar(x='date', y='last_available_death_rate', figsize=(25,10))
st.pyplot()
