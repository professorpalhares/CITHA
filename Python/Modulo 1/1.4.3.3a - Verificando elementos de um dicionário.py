produto = {
    'Nome': ['Feijão','Arroz', 'Farinha'],
    'Quantidade': [10,10, 100]
}

# Verificando os itens do dicionário
for chave, valor in produto.items():
  print(chave, valor)

# Verificando os itens da chave nome
for item in produto['Nome']:
  print(item)