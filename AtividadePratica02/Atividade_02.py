def calcular_desconto(preco_original, percentual_desconto):
    valor_desconto = round(preco_original * (percentual_desconto / 100), 2)
    preco_final = round(preco_original - valor_desconto, 2)
    return valor_desconto, preco_final

nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto, preco_final = calcular_desconto(preco_original, percentual_desconto)

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", percentual_desconto, "%")
print("Valor do desconto: R$", valor_desconto)
print("Preço final: R$", preco_final)
