def saudar(nome):
    """ Uma função que apenas realiza uma ação (imprimir) e não retorna nada. """
    print(f"Olá, {nome}! Seja bem-vindo(a) ao projeto CITHA.")

resultado = saudar("Estudante")

print(f"\nO valor retornado pela função saudar é: {resultado}")
print(f"O tipo do valor retornado é: {type(resultado)}")