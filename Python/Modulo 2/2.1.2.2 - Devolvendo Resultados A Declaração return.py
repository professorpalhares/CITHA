def calcular_valor_lote(quantidade_latas, preco_por_lata):
    """ Calcula o valor total de um lote de castanhas. """
    valor_total = quantidade_latas * preco_por_lata
    return valor_total

# --- Programa Principal ---

# Coletando os dados
latas_vendidas = 50
preco_atual = 35.75 # Preço por lata

# Chamando a função e armazenando o resultado
valor_a_pagar = calcular_valor_lote(latas_vendidas, preco_atual)

# Usando o valor retornado em outra parte do código
print("--- Recibo Simples ---")
print(f"Quantidade: {latas_vendidas} latas")
print(f"Preço por Lata: R$ {preco_atual}")
print(f"Valor Total a Pagar: R$ {valor_a_pagar:.2f}")