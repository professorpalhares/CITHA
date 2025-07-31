import pandas as pd

df_peixes = pd.read_csv("dados_piscicultura.csv", sep=';')

# Passo 2: Análise de Produção por Peixe
print("--- 1. Análise de Produção por Peixe ---")

# Agrupando por peixe e calculando a soma e a média da produção
analise_producao = df_peixes.groupby('PEIXE')['PRODUÇÃO'].agg(['sum', 'mean'])
analise_producao = analise_producao.rename(columns={'sum': 'Produção Total (kg)', 'mean': 'Produção Média Mensal (kg)'})

print(analise_producao.round(2))