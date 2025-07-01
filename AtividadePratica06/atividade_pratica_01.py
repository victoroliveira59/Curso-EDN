import random
import string

def gerar_senha(tamanho):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    qtd = int(input("Informe a quantidade de caracteres da senha: "))
    if qtd <= 0:
        print("A quantidade deve ser maior que zero.")
    else:
        senha = gerar_senha(qtd)
        print("Senha gerada:", senha)
except ValueError:
    print("Entrada inválida! Digite um número inteiro.")
