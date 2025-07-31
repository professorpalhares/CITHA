def descrever_especie(nome_popular, nome_cientifico, altura_media):
    """ Descreve uma espécie de árvore com base em seus dados. """
    print(f"--- Ficha da Espécie ---")
    print(f"Nome Popular: {nome_popular}")
    print(f"Nome Científico: {nome_cientifico}")
    print(f"Altura Média: {altura_media} metros\n")

# Usando argumentos nomeados, a ordem não importa
print("Chamada 1 (ordem misturada):")
descrever_especie(altura_media=25, nome_popular="Açaí", nome_cientifico="Euterpe oleracea")

# Você também pode misturar posicionais e nomeados
# Desde que os posicionais venham primeiro!
print("Chamada 2 (mista):")
descrever_especie("Castanheira", altura_media=50, nome_cientifico="Bertholletia excelsa")