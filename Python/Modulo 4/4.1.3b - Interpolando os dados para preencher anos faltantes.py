import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados_agricolas.csv")

df_agrupado = df.groupby(['ano', 'tipo_cultivo'])['produtividade'].mean().unstack()

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