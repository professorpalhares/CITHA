import pandas as pd

# Especificamos que o delimitador é um ponto e vírgula
df_solo = pd.read_csv('dados_solo.csv', delimiter=';')

print("Dados de Qualidade do Solo:")
print(df_solo)