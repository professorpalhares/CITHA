import pandas as pd

dados_lagos = {
    'especies_peixes': [120, 85, 98],
    'ph_agua': [6.5, 6.8, 6.2],
    'turbidez_ntu': [4.5, 3.1, 5.8]
}
nomes_lagos = ["Lago do Puraquequara", "Lago do Janauari", "Lago do Tarumã-Açu"]
df_lagos = pd.DataFrame(dados_lagos, index=nomes_lagos)

# Selecionando a primeira linha (posição 0) do df_peixes
primeira_linha = df_lagos.iloc[0]
print("--- Primeira Linha do DataFrame (posição 0) ---")
print(primeira_linha)

# Selecionando a terceira linha (posição 2)
terceira_linha = df_lagos.iloc[2]
print("\n--- Terceira Linha do DataFrame (posição 2) ---")
print(terceira_linha)

# Selecionando um intervalo de linhas (da posição 1 à 2)
intervalo_linhas = df_lagos.iloc[1:3]
print("\n--- Linhas da Posição 1 até a 2 ---")
print(intervalo_linhas)