import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')

# --- DADOS ---
dados = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'nivel_m': [18.5, 22.1, 25.7, 28.2, 29.5, 29.1, 27.3, 24.6, 21.0, 18.9, 17.8, 18.1],
    'precipitacao_mm': [310, 300, 320, 250, 180, 90, 60, 40, 70, 120, 150, 210]
}
df = pd.DataFrame(dados)

# --- CRIAÇÃO DOS SUBPLOTS ---
# Figura com 2 linhas e 1 coluna. 'sharex=True' alinha os meses.
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True)

# Adiciona um título geral para a figura inteira
fig.suptitle('Análise Sazonal: Chuva vs. Nível do Rio', fontsize=16, fontweight='bold')

# PLOT 1: Gráfico de Barras da Chuva (no 1º eixo: axes[0])
axes[0].bar(df['mes'], df['precipitacao_mm'], color='royalblue', label='Chuva')
axes[0].set_ylabel('Precipitação (mm)')
axes[0].legend()

# PLOT 2: Gráfico de Linha do Nível do Rio (no 2º eixo: axes[1])
axes[1].plot(df['mes'], df['nivel_m'], color='darkorange', marker='o', label='Nível do Rio')
axes[1].set_ylabel('Nível (metros)')
axes[1].set_xlabel('Mês')
axes[1].legend()

# Ajustes finais
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Espaço para o subtitle
plt.show()