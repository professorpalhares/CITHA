participantes = {"Ana", "Bia", "Carlos"}
print(f"Participantes iniciais\n {participantes} \n")

# Adicionando um novo participante
participantes.add("Daniel")
print(f"Apos adicionar 'Daniel'\n {participantes} \n")

# Tentar adicionar um participante que ja existe
participantes.add("Ana")
print(f"Apos tentar readicionar 'Ana'\n {participantes} \n")

# Removendo um participante
participantes.remove("Bia")
print(f"Apos remover 'Bia'\n {participantes}")