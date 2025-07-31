dados_coleta = [
    {'local': 'Foz do Igarapé', 'turbidez': 4.8},
    {'local': 'Comunidade Ribeirinha', 'turbidez': 2.1},
    {'local': 'Reserva Florestal', 'turbidez': 1.5},
    {'local': 'Ponto de Descarte', 'turbidez': 7.9}
]

# Usando lambda como a "chave" de ordenação para o método sort()
dados_coleta.sort(key=lambda item: item['turbidez'])

print("Dados ordenados por turbidez da água:")
for ponto in dados_coleta:
    print(ponto)