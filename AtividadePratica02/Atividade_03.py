def CalculoMedia(nota_01,nota_02,nota_03):
		media_nota = (nota_01 + nota_02 + nota_03) / 3
		if media_nota >= 7:
			return "Aprovado"
		elif media_nota >= 5:
			return "Recuperação"
		else:
			return "Reprovado"
nota_01 = 7.5
nota_02 = 8.0
nota_03 = 6.5
resultado = CalculoMedia(nota_01, nota_02, nota_03)
print(f"Resultado da média:", resultado)

print(f"Nota 01: {nota_01} / Nota 02: {nota_02} / Nota 03: {nota_03}")
