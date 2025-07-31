import pandas as pd

df_peixes = pd.read_csv('coleta_peixes.csv')

# Obtendo um resumo completo do DataFrame
print("--- Resumo técnico do DataFrame com .info() ---")
df_peixes.info()