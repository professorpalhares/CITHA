import pandas as pd

# DataFrame com nomes de colunas pouco claros
dados_sensor = {
    'location': ['Encontro das Águas', 'Lago Janauari'],
    'ph_val': [6.8, 7.1],
    'turb_ntu': [5.2, 3.1]
}
df_sensor = pd.DataFrame(dados_sensor)

# Usamos .rename() com um dicionário para mapear os nomes antigos para os novos
df_sensor_renomeado = df_sensor.rename(columns={
    'location': 'local_coleta',
    'ph_val': 'valor_ph',
    'turb_ntu': 'turbidez_ntu'
})

print("--- DataFrame Original ---")
print(df_sensor)

print("\n--- DataFrame com Colunas Renomeadas ---")
print(df_sensor_renomeado)