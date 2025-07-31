import pandas as pd
import matplotlib.pyplot as plt

# --- DADOS ---
dados_rio = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
            'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'nivel_m': [18.5, 22.1, 25.7, 28.2, 29.5, 29.1, 27.3, 24.6, 21.0, 18.9, 17.8, 18.1]
}
df_rio = pd.DataFrame(dados_rio)

# --- PASSO 1: Usando um Estilo Profissional ---
# Esta única linha melhora drasticamente a aparência do gráfico.
plt.style.use('ggplot')

# --- PASSO 2: Criação da Figura e do Gráfico Base ---
# `plt.subplots` cria a "tela" (fig) e os "eixos" (ax) separados.
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(df_rio['mes'], df_rio['nivel_m'], marker='o', linestyle='-', color='royalblue', label='Nível Médio do Rio')

# --- PASSO 3: Adicionando Contexto com Linhas de Referência ---
# `axhline` desenha uma linha para marcar um limiar importante.
ax.axhline(y=28.0, color='red', linestyle='--', linewidth=2, label='Nível de Alerta de Enchente')

# --- PASSO 4: Adicionando Narrativa com Anotações ---
# `annotate` permite adicionar texto e setas para destacar pontos.
pico_mes_index = 4 # Índice do mês de Maio
pico_valor = 29.5
ax.annotate('Pico da Cheia', xy=(pico_mes_index, pico_valor), xytext=(pico_mes_index - 2, pico_valor - 0.5), arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8), fontsize=12, fontweight='bold')

# --- PASSO 5: Títulos, Rótulos e Legendas ---
ax.set_title('Monitoramento do Nível do Rio na Bacia Amazônica (2024)', fontsize=16)
ax.set_ylabel('Nível (metros)', fontsize=12)
ax.set_xlabel('Mês', fontsize=12)
plt.xticks(rotation=45)

# Ativa a legenda para identificar as linhas plotadas com 'label'
ax.legend()

# Ajustes finais para garantir que nada seja cortado
plt.tight_layout()
plt.show()