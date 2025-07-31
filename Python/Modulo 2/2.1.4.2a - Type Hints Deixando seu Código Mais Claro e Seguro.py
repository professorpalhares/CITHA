def estimar_biomassa_arvore_com_tipos(especie: str, diametro_cm: float) -> float:
    """Estima a biomassa de uma árvore com base em sua espécie e diâmetro.

    Args:
        especie (str): O nome popular da espécie da árvore
        diametro_cm (float): O diâmetro do tronco medido à altura do peito (DAP), em centímetros.

    Returns:
        float: A biomassa estimada da árvore em quilogramas (kg)"""
    if especie == "Sumaúma":
        fator = 0.65
    else:
        fator = 0.55

    biomassa_kg = fator * (diametro_cm ** 2)
    return biomassa_kg

# Chamada correta
biomassa_castanheira = estimar_biomassa_arvore_com_tipos("Castanheira", 120.5)
print(f"Biomassa da Castanheira: {biomassa_castanheira:.2f} kg")

# O que acontece se passarmos os tipos errados?
# O código AINDA RODA, mas um verificador de tipos acusaria um erro aqui!
biomassa_errada = estimar_biomassa_arvore_com_tipos(150.0, "Açaí")
print(f"Resultado da chamada incorreta: {biomassa_errada}")