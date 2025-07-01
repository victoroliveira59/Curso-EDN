def calcular_idade_em_dias(ano_nascimento, ano_atual):

    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
print(f"Idade aproximada em dias: {idade_dias}")
