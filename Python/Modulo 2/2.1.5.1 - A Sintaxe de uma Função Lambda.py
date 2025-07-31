# Usando uma função def tradicional
def calcular_raio(diametro):
    return diametro / 2

# A mesma lógica com uma função lambda
calcular_raio_lambda = lambda diametro: diametro / 2

# Vamos testar as duas
diametro_arvore = 90 # em cm
print(f"Raio (calculado com def): {calcular_raio(diametro_arvore)} cm")
print(f"Raio (calculado com lambda): {calcular_raio_lambda(diametro_arvore)} cm")