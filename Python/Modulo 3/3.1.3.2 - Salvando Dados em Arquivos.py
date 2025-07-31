import pandas as pd

df_acai = pd.read_csv('producao_acai.csv')

# Agrupamos os dados por local e calculamos a média da produção
resumo_producao = df_acai.groupby('local')['producao_toneladas'].mean().reset_index()

print("Resumo a ser salvo:")
print(resumo_producao)

# Salvando o DataFrame em um novo arquivo CSV
resumo_producao.to_csv('resumo_acai_por_estado.csv')

print("\nArquivo 'resumo_acai_por_estado.csv' salvo com sucesso!")