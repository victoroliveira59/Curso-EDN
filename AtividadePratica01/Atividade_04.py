def CalcularPrecoTotal():
	return  preco_unitario * quantidade

nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = CalcularPrecoTotal()

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)
