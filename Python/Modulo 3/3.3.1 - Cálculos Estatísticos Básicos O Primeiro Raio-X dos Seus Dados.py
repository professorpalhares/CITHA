import pandas as pd
import numpy as np

# Recriando o DataFrame já com os dados ausentes tratados
dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, 0.0], # NaN preenchido com 0
    'ph_agua': [6.8, 6.5, 7.1, 6.82, 6.6, 7.0, 6.9] # NaN preenchido com a média
}
df_peixes = pd.DataFrame(dados)

# 1. Qual a quantidade total de peixes avistados? .sum()
total_peixes = df_peixes['quantidade'].sum()
print(f"Total de peixes avistados: {total_peixes}")

# 2. Qual foi a média de pH da água? .mean()
media_ph = df_peixes['ph_agua'].mean()
print(f"Média do pH da água: {media_ph:.2f}")

# 3. Qual o valor mediano da contagem de peixes? .median()
mediana_peixes = df_peixes['quantidade'].median()
print(f"Mediana da quantidade de peixes: {mediana_peixes}")

# 4. Qual foi a maior e a menor quantidade de peixes registrada? .max() e .min()
max_peixes = df_peixes['quantidade'].max()
min_peixes = df_peixes['quantidade'].min()
print(f"Maior contagem em um local: {max_peixes}")
print(f"Menor contagem em um local: {min_peixes}")

# 5. Quantas medições de pH foram realizadas? .count()
contagem_medicoes = df_peixes['ph_agua'].count()
print(f"Total de medições de pH: {contagem_medicoes}")