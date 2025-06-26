def converter_temperatura(valor, unidade_origem, unidade_destino):
    # Converte a temperatura para Celsius
    if unidade_origem == "C":
        temp_c = valor
    elif unidade_origem == "F":
        temp_c = (valor - 32) * 5/9
    elif unidade_origem == "K":
        temp_c = valor - 273.15
    else:
        return "Unidade de origem inválida"

    # Converte de Celsius para a unidade de destino
    if unidade_destino == "C":
        return round(temp_c, 2)
    elif unidade_destino == "F":
        return round((temp_c * 9/5) + 32, 2)
    elif unidade_destino == "K":
        return round(temp_c + 273.15, 2)
    else:
        return "Unidade de destino inválida"

valor = float(input("Informe a temperatura: "))
unidade_origem = input("Unidade de origem (C/F/K): ").upper()
unidade_destino = input("Unidade de destino (C/F/K): ").upper()

resultado = converter_temperatura(valor, unidade_origem, unidade_destino)

print(f"{valor}°{unidade_origem} equivale a {resultado}°{unidade_destino}")
