import pandas as pd

# Criando um DataFrame com os dados da pesquisa de campo
dados_floresta = {
    'id': ['A1', 'A2', 'B1', 'B2'],
    'quantidade': [450, 510, 480, 530],
    'area': [2.0, 2.2, 2.1, 2.3]
}
df_floresta = pd.DataFrame(dados_floresta)

print("--- DataFrame Original ---")
print(df_floresta)

# Criando a nova coluna 'densidade_arvores'
# A operação é feita para todas as linhas de uma só vez!
df_floresta['densidade'] = df_floresta['quantidade'] / df_floresta['area']

print("\n--- DataFrame com a Nova Coluna de Densidade ---")
print(df_floresta)