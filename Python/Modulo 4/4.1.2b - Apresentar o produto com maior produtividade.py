import pandas as pd

df = pd.read_csv("dados_agricolas.csv")

produtividade_media = df.groupby('tipo_cultivo')['produtividade'].mean().reset_index()

# Passo 3: Apresentar o produto com maior produtividade
print("\n--- 3. Cultivo com Maior Produtividade Média ---")
cultivo_mais_produtivo = produtividade_media.loc[produtividade_media['produtividade'].idxmax()]
print(cultivo_mais_produtivo)