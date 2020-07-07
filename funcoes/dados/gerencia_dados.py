import pandas as pd


def csv_para_dataframe():
    df = pd.read_csv("dados/covid19.csv", sep=',')
    df.reset_index(inplace=True)
    df.dropna(inplace=True)
    return df


def gera_amostra(df):
    amostra = df.sample(n=4081)
    return amostra


def gera_exploracao(df):
    exploracao = pd.DataFrame({'nomes': df.columns,
                               'tipos': df.dtypes,
                               'NA #': df.isna().sum(),
                               'NA %': (df.isna().sum() / df.shape[0]) * 100})
    return exploracao


def filtra_dados_sao_jose_dos_campos(df):
    df_sao_jose_dos_campos = df[df.city_ibge_code.eq(3549904)]
    df_sao_jose_dos_campos.sort_values('date', ascending=True, inplace=True)
    return df_sao_jose_dos_campos


