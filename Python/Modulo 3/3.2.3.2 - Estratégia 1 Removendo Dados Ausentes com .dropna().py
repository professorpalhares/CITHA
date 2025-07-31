import pandas as pd
import numpy as np # Usaremos numpy para inserir NaN de forma controlada

# Recriando nosso DataFrame para o exemplo
dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, np.nan],
    'ph_agua': [6.8, 6.5, 7.1, np.nan, 6.6, 7.0, 6.9]
}
df_peixes = pd.DataFrame(dados)

# Criando uma cópia limpa do DataFrame removendo todas as linhas
# que contenham pelo menos um valor NaN.
df_completo = df_peixes.dropna()

print("--- DataFrame Original ---")
print(df_peixes)

print("\n--- DataFrame Após .dropna() ---")
print(df_completo)