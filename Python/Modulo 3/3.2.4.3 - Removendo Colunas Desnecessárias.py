import pandas as pd

# DataFrame com colunas a serem removidas
dados_completos = {
    'cod_coleta': ['C01', 'C02', 'C03'],
    'local': ['Parintins', 'Maués', 'Itacoatiara'],
    'especie': ['Tambaqui', 'Pirarucu', 'Tucunaré'],
    'timestamp': [1672531200, 1672617600, 1672704000]
}
df_completo = pd.DataFrame(dados_completos)

# Removendo uma lista de colunas com o método .drop()
# O argumento 'axis=1' informa ao Pandas que queremos remover colunas, não linhas
df_simplificado = df_completo.drop(columns=['cod_coleta', 'timestamp'])

print("--- DataFrame Original ---")
print(df_completo)

print("\n--- DataFrame Após Remover Colunas ---")
print(df_simplificado)