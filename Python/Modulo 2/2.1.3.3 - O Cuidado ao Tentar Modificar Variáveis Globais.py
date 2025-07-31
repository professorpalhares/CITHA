contador_alertas = 0 # Global

def registrar_alerta(tipo_alerta):
    print(f"\n ALERTA REGISTRADO: {tipo_alerta}")
    # Aqui, Python cria uma NOVA variável 'contador_alertas' que é LOCAL
    contador_alertas = 1
    print(f"-> Contagem local de alertas nesta função: {contador_alertas}")

print(f"Contagem total de alertas ANTES da chamada: {contador_alertas}")
registrar_alerta("Nível do rio muito alto")
print(f"Contagem total de alertas DEPOIS da chamada: {contador_alertas}")