def analisar_temperaturas(medicoes):
    """ Encontra a temperatura mínima e máxima de uma lista de medições. """
    if not medicoes: # Verifica se a lista não está vazia
        return (None, None) # Retorna None se não houver dados

    minima = min(medicoes)
    maxima = max(medicoes)
    return minima, maxima # Retorna os dois valores

# Lista de temperaturas coletadas durante uma semana
temperaturas_semana = [28.5, 29.1, 31.2, 27.8, 30.5, 32.0, 29.9]

# Chamando a função e "desempacotando" o resultado em duas variáveis
temp_min, temp_max = analisar_temperaturas(temperaturas_semana)

print(f"Análise da Semana:")
print(f"  - Temperatura Mínima: {temp_min}°C")
print(f"  - Temperatura Máxima: {temp_max}°C")

# O que acontece se chamarmos com uma lista vazia?
min_vazia, max_vazia = analisar_temperaturas([])
print(f"\nAnálise de lista vazia: {min_vazia}, {max_vazia}")