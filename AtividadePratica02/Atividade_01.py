def converter_moeda(valor_reais, taxa_dolar, taxa_euro):
    valor_dolar = round(valor_reais / taxa_dolar, 2)
    valor_euro = round(valor_reais / taxa_euro, 2)
    return valor_dolar, valor_euro

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

dolar, euro = converter_moeda(valor_reais, taxa_dolar, taxa_euro)

print("Valor em reais: R$", valor_reais)
print("Valor em dólares: US$", dolar)
print("Valor em euros: €",euro)
