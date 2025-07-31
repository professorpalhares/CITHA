import pandas as pd

df_peixes = pd.read_csv('coleta_peixes.csv')

# Mostrando as 3 primeiras linhas
print("--- Primeiras 3 linhas com .head(3) ---")
print(df_peixes.head(3))

# Mostrando as 2 últimas linhas
print("\n--- Últimas 2 linhas com .tail(2) ---")
print(df_peixes.tail(2))