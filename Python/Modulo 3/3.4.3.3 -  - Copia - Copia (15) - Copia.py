import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Para garantir que nossos exemplos sejam reprodutíveis, vamos criar os dados
np.random.seed(42) # Semente para reprodutibilidade
dados = {
    'id_arvore': range(1, 101),
    'regiao': np.random.choice(['Reserva Tapajós', 'Floresta Jari'], 100),
    'diametro_cm': np.random.normal(loc=120, scale=25, size=100),
    'producao_kg': np.nan # Vamos preencher com base no diâmetro
}
df_safra = pd.DataFrame(dados)

# Criando uma relação realista entre diâmetro e produção com um pouco de ruído
df_safra['producao_kg'] = (df_safra['diametro_cm'] * 0.45) + np.random.normal(loc=0, scale=10, size=100)
# Garantindo que não haja produção negativa
df_safra['producao_kg'] = df_safra['producao_kg'].clip(lower=5)

# O Pandas tem uma integração direta para criar boxplots por categoria
fig, ax = plt.subplots(figsize=(10, 7))

# Usamos o método .boxplot() do DataFrame
# 'column' é a variável que queremos analisar
# 'by' é a categoria pela qual queremos agrupar
df_safra.boxplot(column='producao_kg', by='regiao', ax=ax, grid=False)

# Customizando o gráfico
ax.set_title('Comparação da Produção de Castanha por Região', fontsize=16)
ax.set_ylabel('Produção por Árvore (kg)', fontsize=12)
ax.set_xlabel('Região de Coleta', fontsize=12)
fig.suptitle('') # Remove o título automático do pandas

plt.show()