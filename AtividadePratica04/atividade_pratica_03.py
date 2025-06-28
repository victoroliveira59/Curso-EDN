def senha_forte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ").strip()
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    if senha_forte(senha):
        print("Senha forte cadastrada com sucesso!")
        break
    else:
        print("Senha fraca! A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
