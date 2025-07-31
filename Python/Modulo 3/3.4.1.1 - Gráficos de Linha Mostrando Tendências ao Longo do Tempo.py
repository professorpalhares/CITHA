import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados para um DataFrame
df_rio = pd.read_csv('nivel_rio.csv')

# Criar o gráfico de linha usando o método .plot() do Pandas
# O Pandas usa o Matplotlib por baixo dos panos para criar o gráfico
df_rio.plot(kind='line', x='mes', y='nivel_m', marker='o')

# Customizando o gráfico com funções do Matplotlib
plt.title('Nível Médio Mensal do Rio na Bacia Amazônica')
plt.xlabel('Mês')
plt.ylabel('Nível (metros)')
plt.xticks(ticks=df_rio.index, labels=df_rio['mes'], rotation=45) # Incluí os meses como rótulo do eixo x e rotaciona para melhor vizualização
plt.grid(True) # Adiciona uma grade para facilitar a leitura
plt.tight_layout() # Ajusta o gráfico para caber tudo

# Exibir o gráfico
plt.show()