def calcular_densidade_arvores(contagem_arvores, area_hectares):
    """Calcula a densidade de árvores por hectare."""
    # 'densidade' é uma variável de escopo local.
    # Ela só existe dentro desta função.
    densidade = contagem_arvores / area_hectares
    print(f"-> Dentro da função: A densidade calculada é de {densidade:.2f} árvores/ha.")
    return densidade

# --- Programa Principal ---
print("Iniciando a análise da Parcela 1...")
densidade_parcela1 = calcular_densidade_arvores(520, 2) # 520 árvores em 2 hectares
print(f"Fora da função: O resultado retornado foi {densidade_parcela1:.2f}.\n")

# Agora, vamos tentar acessar a variável 'densidade' diretamente.
print("Tentando acessar a variável 'densidade' fora da função...")
print(densidade)