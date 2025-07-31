import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_agricolas.csv")

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