import pandas as pd

# Passo 1: Leitura e Inspeção Inicial dos Dados
# Para carregar os dados nesse arquivo, é preciso especificar o separador como ponto e vírgula
df_peixes = pd.read_csv("dados_piscicultura.csv", sep=';')

print("--- Dados de Piscicultura Carregados ---")
print(df_peixes.head())

print("\n--- Informações e Estrutura do DataFrame ---")
df_peixes.info()