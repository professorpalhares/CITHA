def estimar_biomassa_arvore(especie, diametro_cm):
    """Estima a biomassa de uma árvore com base em sua espécie e diâmetro. Utiliza um fator de conversão simplificado que varia conforme a espécie para calcular a biomassa acima do solo. Não é um modelo científico preciso, mas serve como exemplo.

    Args:
        especie (str): O nome popular da espécie da árvore.
        diametro_cm (float): O diâmetro do tronco medido à altura do peito (DAP), em centímetros.

    Returns:
        float: A biomassa estimada da árvore em quilogramas (kg)."""
    if especie == "Sumaúma":
        fator = 0.65
    else:
        fator = 0.55  # Fator genérico para outras espécies

    # Fórmula simplificada: biomassa = fator * (diametro^2)
    biomassa_kg = fator * (diametro_cm ** 2)
    return biomassa_kg

# Agora, vamos ver como acessar nossa documentação
help(estimar_biomassa_arvore)