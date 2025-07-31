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

# Gerando o resumo estatístico completo
resumo_estatistico = df_peixes.describe()

print("--- Resumo Estatístico do DataFrame ---")
print(resumo_estatistico)