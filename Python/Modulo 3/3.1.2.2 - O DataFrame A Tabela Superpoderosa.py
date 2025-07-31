import pandas as pd

# Dicionário com os dados da pesquisa
dados_lagos = {
    'especies_peixes': [120, 85, 98],
    'ph_agua': [6.5, 6.8, 6.2],
    'turbidez_ntu': [4.5, 3.1, 5.8]
}

# Lista com os nomes dos lagos para usar como índice
nomes_lagos = ["Lago do Puraquequara", "Lago do Janauari", "Lago do Tarumã-Açu"]

# Criando o DataFrame
df_lagos = pd.DataFrame(dados_lagos, index=nomes_lagos)

print("Tabela de Monitoramento da Qualidade da Água e Biodiversidade:")
print(df_lagos)

# Selecionando uma única coluna do DataFrame
coluna_ph = df_lagos['ph_agua']

print("\nA coluna 'ph_agua' é do tipo:")
print(type(coluna_ph))
print("\nConteúdo da coluna:")
print(coluna_ph)