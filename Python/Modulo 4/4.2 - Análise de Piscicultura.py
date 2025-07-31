import pandas as pd

# Passo 1: Leitura e Inspeção Inicial dos Dados
# Para carregar os dados nesse arquivo, é preciso especificar o separador como ponto e vírgula
df_peixes = pd.read_csv("dados_piscicultura.csv", sep=';')

print("--- Dados de Piscicultura Carregados ---")
print(df_peixes.head())

print("\n--- Informações e Estrutura do DataFrame ---")
df_peixes.info()

#-*-*-*-*-*-*-*-*-*-

# Passo 2: Análise de Produção por Peixe
print("--- 1. Análise de Produção por Peixe ---")

# Agrupando por peixe e calculando a soma e a média da produção
analise_producao = df_peixes.groupby('PEIXE')['PRODUÇÃO'].agg(['sum', 'mean'])
analise_producao = analise_producao.rename(columns={'sum': 'Produção Total (kg)', 'mean': 'Produção Média Mensal (kg)'})

print(analise_producao.round(2))

#-*-*-*-*-*-*-*-*-*-

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

#-*-*-*-*-*-*-*-*-*-

import matplotlib.pyplot as plt

# Passo 4: Gerando visualização integrada (Produção vs. Custo)
# --- Preparando os dados para pivotar ---
df_prod_pivot = df_peixes.pivot(index='MES', columns='PEIXE', values='PRODUÇÃO')
df_custo_pivot = df_peixes.pivot(index='MES', columns='PEIXE', values='CUSTO_TOTAL_MES')

# Ordenando os meses
meses_ordem = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
df_prod_pivot = df_prod_pivot.reindex(meses_ordem)
df_custo_pivot = df_custo_pivot.reindex(meses_ordem)

# --- Criando a figura com 2 subplots ---
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)
fig.suptitle('Análise Operacional e Financeira da Piscicultura', fontsize=18, fontweight='bold')

# --- Plot 1: Produção Mensal (kg) ---
df_prod_pivot.plot(kind='line', marker='o', ax=axes[0])
axes[0].set_title('Ciclo de Produção Mensal', fontsize=14)
axes[0].set_ylabel('Produção (kg)')
axes[0].legend(title='Peixe')
axes[0].grid(True, linestyle='--', linewidth=0.5)

# --- Plot 2: Custo Total Mensal (R$) ---
df_custo_pivot.plot(kind='line', marker='o', ax=axes[1])
axes[1].set_title('Custo Total de Produção Mensal', fontsize=14)
axes[1].set_ylabel('Custo Total (R$)')
axes[1].set_xlabel('Mês')
axes[1].legend(title='Peixe')
axes[1].grid(True, linestyle='--', linewidth=0.5)

# Ajustes finais
plt.xticks(ticks=range(len(meses_ordem)), labels=meses_ordem, rotation=45)
plt.tight_layout(rect=[0, 0, 1, 0.95]) # Ajusta o super-título
plt.show()