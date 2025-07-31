import pandas as pd

# Criando uma Series a partir de uma lista Python
dados_peixes = [120, 85, 98]
lagos = ["Lago do Puraquequara", "Lago do Janauari", "Lago do Tarumã-Açu"]

# Criando a Series com índices personalizados
s_peixes = pd.Series(data=dados_peixes, index=lagos)

print("Dados da Contagem de Espécies de Peixes:")
print(s_peixes)