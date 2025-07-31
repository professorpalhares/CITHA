import pandas as pd
import matplotlib.pyplot as plt

# Recriando o DataFrame de peixes já limpo
dados = {
    'local': ['Encontro das Águas', 'Frente a Manaus', 'Lago Janauari', 'Parintins', 'Frente a Manaus', 'Lago Janauari', 'Encontro das Águas'],
    'especie': ['Tambaqui', 'Tucunaré', 'Pirarucu', 'Tambaqui', 'Jaraqui', 'Tucunaré', 'Pirarucu'],
    'quantidade': [45.0, 22.0, 10.0, 56.0, 89.0, 15.0, 0.0]
}
df_peixes = pd.DataFrame(dados)

# 1. Agrupar os dados para obter a soma por espécie (Análise)
contagem_por_especie = df_peixes.groupby('especie')['quantidade'].sum()

# 2. Criar o gráfico de barras a partir do resultado (Visualização)
contagem_por_especie.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'gold'])

# 3. Customizar e exibir o gráfico
plt.title('Contagem Total de Peixes por Espécie')
plt.xlabel('Espécie')
plt.ylabel('Quantidade Total Contada')
plt.xticks(rotation=0) # Mantém os nomes das espécies na horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()