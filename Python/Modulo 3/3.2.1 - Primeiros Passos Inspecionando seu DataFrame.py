import pandas as pd

# Carregando os dados do arquivo CSV para o nosso DataFrame
df_peixes = pd.read_csv('coleta_peixes.csv')

# Exibindo o DataFrame completo para confirmar que carregou
print(df_peixes)