produto = { 'Nome': ['Feijão','Arroz', 'Farinha'],
           'Quantidade': [10,10, 100]}

for nome,quantidade in zip(produto['Nome'],produto['Quantidade']):
  print("Produto:", nome, "Quantidade : ",quantidade )