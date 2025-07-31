import pandas as pd

df = pd.read_csv("dados_agricolas.csv")

print("--- Dados carregados com sucesso a partir da URL! ---")
# Visualizando as 5 primeiras linhas
print(df.head())

# Obtendo informações gerais do DataFrame
print("\n--- Informações e Estrutura do DataFrame ---")
df.info()