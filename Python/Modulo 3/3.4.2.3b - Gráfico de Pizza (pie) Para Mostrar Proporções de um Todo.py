import pandas as pd
import matplotlib.pyplot as plt

# Recriando o DataFrame de peixes já limpo
dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, 0.0]
}
df_peixes = pd.DataFrame(dados)

# 1. Agrupar os dados para obter a média por local e ordenar as barras de forma decrescente (maior para o menor)
contagem_por_local = df_peixes.groupby('local')['quantidade'].mean().sort_values()

contagem_por_local.plot(
    kind='pie', # Estilo do gráfico
    y='quantidade', # Quais dados serão usados nas porcentagens
    autopct='%1.1f%%', # Mostra as porcentagens
    figsize=(6, 6), # Tamanho do gráfico
    legend=False, # Nesse caso é desnecessário
    labels=contagem_por_local.index, # Rótulos dos locais
    colors=['skyblue', 'salmon', 'lightgreen', 'gold']
)
plt.title('Composição Relativa da Média de Peixes Coletados')
plt.ylabel('') # Remove o rótulo 'quantidade' que é desnecessário
plt.show()