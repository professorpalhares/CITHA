import pandas as pd

# Usamos a função read_csv para ler o arquivo
# O Pandas identifica automaticamente o cabeçalho e as colunas
df_acai = pd.read_csv('producao_acai.csv')

# Vamos imprimir o DataFrame para ver o resultado
print("Dados de Produção de Açaí:")
print(df_acai)