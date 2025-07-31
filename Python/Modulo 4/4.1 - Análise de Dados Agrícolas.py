import pandas as pd

# Passo 1: Leitura e Inspeção Inicial dos Dados
df = pd.read_csv("dados_agricolas.csv")

print("--- Dados carregados com sucesso a partir da URL! ---")
# Visualizando as 5 primeiras linhas
print(df.head())

# Obtendo informações gerais do DataFrame
print("\n--- Informações e Estrutura do DataFrame ---")
df.info()

#-*-*-*-*-*-*-*-*-*-

# Passo 2: Tabela de produtividade média por produto
print("--- 2. Produtividade Média por Tipo de Cultivo ---")
produtividade_media = df.groupby('tipo_cultivo')['produtividade'].mean().reset_index()
print(produtividade_media.round(2))

#-*-*-*-*-*-*-*-*-*-

# Passo 3: Apresentar o produto com maior produtividade
print("\n--- 3. Cultivo com Maior Produtividade Média ---")
cultivo_mais_produtivo = produtividade_media.loc[produtividade_media['produtividade'].idxmax()]
print(cultivo_mais_produtivo)

#-*-*-*-*-*-*-*-*-*-

# Passo 4: Apresentar o produto com menor uso médio de água
print("\n--- 4. Cultivo com Menor Uso Médio de Água ---")
uso_agua_medio = df.groupby('tipo_cultivo')['uso_agua'].mean().reset_index()
cultivo_menor_uso_agua = uso_agua_medio.loc[uso_agua_medio['uso_agua'].idxmin()]
print(cultivo_menor_uso_agua)

#-*-*-*-*-*-*-*-*-*-

import matplotlib.pyplot as plt

# Passo 5:Gerando gráfico da produtividade
# Agrupando para obter a produtividade média por ano e por cultivo
df_agrupado = df.groupby(['ano', 'tipo_cultivo'])['produtividade'].mean().unstack()

# Criando o gráfico
fig, ax = plt.subplots(figsize=(14, 8))
df_agrupado.plot(kind='line', marker='o', ax=ax)

# Customizando o gráfico
ax.set_title('Produtividade Média por Cultivo', fontsize=16)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Produtividade Média (toneladas/hectare)', fontsize=12)
ax.legend(title='Tipo de Cultivo')
plt.show()

#-*-*-*-*-*-*-*-*-*-

# Interpolando os dados para preencher anos faltantes
df_interpolado = df_agrupado.interpolate(method='linear')

# Criando o gráfico com os dados corrigidos
fig, ax = plt.subplots(figsize=(14, 8))
df_interpolado.plot(kind='line', marker='o', ax=ax)

# Customizando o gráfico final
ax.set_title('Produtividade Média por Cultivo ao Longo dos Anos (com Interpolação)', fontsize=16)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Produtividade Média (toneladas/hectare)', fontsize=12)
ax.legend(title='Tipo de Cultivo')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()