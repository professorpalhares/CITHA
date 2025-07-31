# FATOR_CARBONO é uma variável de escopo global.
# Por convenção, nomes em maiúsculas indicam constantes.
FATOR_CARBONO = 0.5

def estimar_carbono_floresta(biomassa_total_toneladas):
    """Estima o carbono estocado com base na biomassa, usando o fator global."""
    print("-> Acessando a variável global FATOR_CARBONO de dentro da função.")
    # A função PODE LER a variável global sem problemas.
    carbono_estocado = biomassa_total_toneladas * FATOR_CARBONO
    return carbono_estocado

def estimar_carbono_solo(materia_organica_toneladas):
    """Estima o carbono no solo, que também usa o mesmo fator global."""
    print("-> Outra função acessando a mesma variável global.")
    carbono_no_solo = materia_organica_toneladas * FATOR_CARBONO
    return carbono_no_solo


# --- Programa Principal ---
estoque_carbono_floresta = estimar_carbono_floresta(1200)
print(f"Estoque de carbono na floresta: {estoque_carbono_floresta} toneladas.\n")

estoque_carbono_solo = estimar_carbono_solo(350)
print(f"Estoque de carbono no solo: {estoque_carbono_solo} toneladas.")