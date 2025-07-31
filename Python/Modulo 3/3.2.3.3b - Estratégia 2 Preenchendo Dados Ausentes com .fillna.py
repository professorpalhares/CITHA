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

# Criando uma cópia para não alterar o DataFrame original
df_preenchido = df_peixes.copy()

# Preenchendo o NaN na coluna 'quantidade' com o valor 0
df_preenchido['quantidade'] = df_preenchido['quantidade'].fillna(0)

# Primeiro, calculamos a média da coluna (o Pandas ignora os NaNs no cálculo)
media_ph = df_peixes['ph_agua'].mean()
print(f"A média do pH calculada é: {media_ph:.2f}\n")

# Agora, preenchemos o NaN da coluna 'ph_agua' com a média
df_preenchido['ph_agua'] = df_preenchido['ph_agua'].fillna(media_ph)

print(df_preenchido)