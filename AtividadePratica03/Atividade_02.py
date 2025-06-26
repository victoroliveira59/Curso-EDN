def calcular_imc(peso, altura):
    imc = round(peso / (altura ** 2), 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"
    return imc, classificacao

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc, classificacao = calcular_imc(peso, altura)

print("Seu IMC é:", imc)
print("Classificação:", classificacao)
