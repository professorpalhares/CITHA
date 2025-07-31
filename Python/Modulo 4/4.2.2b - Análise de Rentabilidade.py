import pandas as pd

df_peixes = pd.read_csv("dados_piscicultura.csv", sep=';')

# Passo 3: Análise de Custo e Rentabilidade
print("\n--- 2. Análise de Rentabilidade ---")
# Custo Total = Soma(Produção de cada mês * Custo Médio de cada mês)
df_peixes['CUSTO_TOTAL_MES'] = df_peixes['PRODUÇÃO'] * df_peixes['CUSTO_MEDIO']

# Agrupando para obter os totais por peixe
custo_total = df_peixes.groupby('PEIXE')['CUSTO_TOTAL_MES'].sum()
producao_total = df_peixes.groupby('PEIXE')['PRODUÇÃO'].sum()

# Calculando a rentabilidade
rentabilidade = producao_total / custo_total

print("Rentabilidade (kg produzidos por R$ investido):")
print(rentabilidade.round(2))
print(f"\nO peixe mais rentável é o: {rentabilidade.idxmax()}")