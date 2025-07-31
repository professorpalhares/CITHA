def descrever_especie(nome_popular, nome_cientifico, altura_media):
    """ Descreve uma espécie de árvore com base em seus dados. """
    print(f"--- Ficha da Espécie ---")
    print(f"Nome Popular: {nome_popular}")
    print(f"Nome Científico: {nome_cientifico}")
    print(f"Altura Média: {altura_media} metros")

# Chamando a função com argumentos posicionais
descrever_especie("Sumaúma", "Ceiba pentandra", 40)