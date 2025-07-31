import pandas as pd

df = pd.read_csv("dados_agricolas.csv")

# Passo 2: Tabela de produtividade média por produto
print("--- 2. Produtividade Média por Tipo de Cultivo ---")
produtividade_media = df.groupby('tipo_cultivo')['produtividade'].mean().reset_index()
print(produtividade_media.round(2))