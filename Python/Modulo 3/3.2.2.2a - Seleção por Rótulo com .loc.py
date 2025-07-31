import pandas as pd

dados_lagos = {
    'especies_peixes': [120, 85, 98],
    'ph_agua': [6.5, 6.8, 6.2],
    'turbidez_ntu': [4.5, 3.1, 5.8]
}
nomes_lagos = ["Lago do Puraquequara", "Lago do Janauari", "Lago do Tarumã-Açu"]
df_lagos = pd.DataFrame(dados_lagos, index=nomes_lagos)

print("--- DataFrame com Índice Nominal ---")
print(df_lagos)

# Usando .loc para selecionar a linha com o rótulo "Lago do Janauari"
dados_janauari = df_lagos.loc["Lago do Janauari"]

print("\n--- Dados apenas do Lago do Janauari ---")
print(dados_janauari)