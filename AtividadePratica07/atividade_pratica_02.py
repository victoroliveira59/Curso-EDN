import csv
import os

def criar_dados_pessoas():
    """
    Cria uma lista de dados de pessoas para exemplo
    
    Returns:
        list: Lista de dicionários com dados das pessoas
    """
    pessoas = [
        {"Nome": "João Silva", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Maria Santos", "Idade": 35, "Cidade": "Rio de Janeiro"},
        {"Nome": "Pedro Oliveira", "Idade": 22, "Cidade": "Belo Horizonte"},
        {"Nome": "Ana Costa", "Idade": 41, "Cidade": "Brasília"},
        {"Nome": "Carlos Souza", "Idade": 33, "Cidade": "Salvador"},
        {"Nome": "Lucia Pereira", "Idade": 29, "Cidade": "Fortaleza"},
        {"Nome": "Roberto Lima", "Idade": 45, "Cidade": "Recife"},
        {"Nome": "Fernanda Alves", "Idade": 31, "Cidade": "Porto Alegre"},
        {"Nome": "Rafael Campos", "Idade": 26, "Cidade": "Curitiba"},
        {"Nome": "Juliana Rocha", "Idade": 38, "Cidade": "Goiânia"}
    ]
    return pessoas

def escrever_csv_pessoas(nome_arquivo, dados_pessoas):
    """
    Escreve dados de pessoas em um arquivo CSV
    
    Args:
        nome_arquivo (str): Nome do arquivo CSV a ser criado
        dados_pessoas (list): Lista de dicionários com dados das pessoas
    """
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            # Define os nomes das colunas
            colunas = ['Nome', 'Idade', 'Cidade']
            
            # Cria o objeto writer
            escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
            
            # Escreve o cabeçalho
            escritor.writeheader()
            
            # Escreve os dados das pessoas
            escritor.writerows(dados_pessoas)
            
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        print(f"Total de registros escritos: {len(dados_pessoas)}")
        
    except Exception as e:
        print(f"Erro ao criar arquivo CSV: {e}")

def ler_e_exibir_csv(nome_arquivo):
    """
    Lê e exibe o conteúdo do arquivo CSV criado
    
    Args:
        nome_arquivo (str): Nome do arquivo CSV a ser lido
    """
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            
            print(f"\n=== CONTEÚDO DO ARQUIVO '{nome_arquivo}' ===")
            print("-" * 50)
            
            for i, linha in enumerate(leitor, 1):
                print(f"{i:2d}. Nome: {linha['Nome']:<20} | Idade: {linha['Idade']:<3} | Cidade: {linha['Cidade']}")
                
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler arquivo CSV: {e}")

def adicionar_pessoa_interativa(nome_arquivo):
    """
    Permite ao usuário adicionar uma nova pessoa ao arquivo CSV
    
    Args:
        nome_arquivo (str): Nome do arquivo CSV
    """
    try:
        print("\n=== ADICIONAR NOVA PESSOA ===")
        nome = input("Digite o nome: ").strip()
        
        while True:
            try:
                idade = int(input("Digite a idade: ").strip())
                if idade < 0:
                    print("Idade deve ser um número positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número válido para a idade.")
        
        cidade = input("Digite a cidade: ").strip()
        
        # Adiciona a nova pessoa ao arquivo
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.DictWriter(arquivo_csv, fieldnames=['Nome', 'Idade', 'Cidade'])
            escritor.writerow({'Nome': nome, 'Idade': idade, 'Cidade': cidade})
        
        print(f"Pessoa '{nome}' adicionada com sucesso!")
        
    except Exception as e:
        print(f"Erro ao adicionar pessoa: {e}")

def main():
    """
    Função principal do programa
    """
    print("=== GERADOR DE ARQUIVO CSV DE PESSOAS ===\n")
    
    nome_arquivo = "pessoas.csv"
    
    # Pergunta se deve criar arquivo com dados de exemplo
    if not os.path.exists(nome_arquivo):
        print("Arquivo CSV não existe. Criando arquivo com dados de exemplo...")
        dados_exemplo = criar_dados_pessoas()
        escrever_csv_pessoas(nome_arquivo, dados_exemplo)
    else:
        print(f"Arquivo '{nome_arquivo}' já existe.")
    
    # Exibe o conteúdo atual
    ler_e_exibir_csv(nome_arquivo)
    
    # Menu interativo
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar nova pessoa")
        print("2. Exibir conteúdo do arquivo")
        print("3. Criar novo arquivo com dados de exemplo")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            adicionar_pessoa_interativa(nome_arquivo)
        elif opcao == "2":
            ler_e_exibir_csv(nome_arquivo)
        elif opcao == "3":
            resposta = input(f"Isso substituirá o arquivo '{nome_arquivo}' existente. Continuar? (s/n): ").strip().lower()
            if resposta == 's':
                dados_exemplo = criar_dados_pessoas()
                escrever_csv_pessoas(nome_arquivo, dados_exemplo)
                print("Novo arquivo criado com dados de exemplo.")
        elif opcao == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()