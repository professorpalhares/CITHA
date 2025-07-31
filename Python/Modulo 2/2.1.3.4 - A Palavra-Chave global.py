contador_alertas = 0 # Global

def registrar_alerta_global(tipo_alerta):
    global contador_alertas # Avisando ao Python: use a variável global!
    print(f"\n ALERTA REGISTRADO: {tipo_alerta}")
    contador_alertas = contador_alertas + 1
    print(f"-> Contagem de alertas atualizada: {contador_alertas}")

print(f"Contagem inicial: {contador_alertas}")
registrar_alerta_global("Temperatura elevada")
registrar_alerta_global("Desmatamento detectado")
print(f"Contagem final: {contador_alertas}")