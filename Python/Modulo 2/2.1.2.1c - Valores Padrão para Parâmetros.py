def registrar_nivel_rio(nivel_metros, local="Próximo à comunidade ribeirinha"):
    """ Registra a medição do nível de um rio em um local específico. """
    print(f"Medição registrada:")
    print(f"  -> Nível: {nivel_metros} metros")
    print(f"  -> Local: {local}\n")

# Chamada 1: Usando o local padrão
print("--- Medição Padrão ---")
registrar_nivel_rio(3.5)

# Chamada 2: Especificando um local diferente
print("--- Medição em Ponto Específico ---")
registrar_nivel_rio(3.7, local="Foz do igarapé")