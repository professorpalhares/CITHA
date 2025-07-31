# --- Bloco para o Sensor de Umidade ---
umidade = 45.7
print(f"Lendo dado de umidade: {umidade}%")
if not (30 <= umidade <= 70):
    print("ALERTA: Umidade do solo fora do padrão!")
else:
    print("Umidade do solo OK.")
print("-" * 20)

# --- Bloco para o Sensor de Temperatura ---
temperatura = 31.5
print(f"Lendo dado de temperatura: {temperatura}°C")
if not (22 <= temperatura <= 30):
    print("ALERTA: Temperatura do ar fora do padrão!")
else:
    print("Temperatura do ar OK.")
print("-" * 20)

# --- Bloco para o Sensor de pH da Água ---
ph_agua = 5.8
print(f"Lendo dado de pH da água: {ph_agua}")
if not (6.5 <= ph_agua <= 8.5):
    print("ALERTA: pH da água fora do padrão!")
else:
    print("pH da água OK.")
print("-" * 20)