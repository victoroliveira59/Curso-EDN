def eh_palindromo(texto):

    import string
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
