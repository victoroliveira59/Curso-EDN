def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida.")

while True:
    try:
        n1 = input("Digite o primeiro número: ")
        num1 = float(n1)
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")
        continue

    try:
        n2 = input("Digite o segundo número: ")
        num2 = float(n2)
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")
        continue

    operacao = input("Digite a operação (+, -, *, /): ")
    try:
        resultado = calcular(num1, num2, operacao)
    except ZeroDivisionError as e:
        print("Erro:", e)
        continue
    except ValueError as e:
        print("Erro:", e)
        continue

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
    break
