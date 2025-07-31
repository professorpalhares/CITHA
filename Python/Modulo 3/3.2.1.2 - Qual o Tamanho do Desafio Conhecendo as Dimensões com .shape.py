import pandas as pd

df_peixes = pd.read_csv('coleta_peixes.csv')

# Obtendo as dimensões do nosso DataFrame
dimensoes = df_peixes.shape

print(f"O DataFrame tem {dimensoes[0]} linhas (observações) e {dimensoes[1]} colunas (variáveis).")