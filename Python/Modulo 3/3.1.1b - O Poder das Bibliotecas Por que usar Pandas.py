import pandas as pd

# 1. Ler o arquivo CSV diretamente para um DataFrame
# O 'pd' é o apelido padrão para o pandas
df = pd.read_csv('dados_rio.csv')

# 2. Calcular a média da coluna 'temperatura_c'
media_pandas = df['temperatura_c'].mean()

print(f"A temperatura média (calculada com Pandas) é: {media_pandas:.2f}°C")