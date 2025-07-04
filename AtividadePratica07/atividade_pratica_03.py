import csv
import os

def ler_csv_pessoas(nome_arquivo):
    """
    Lê um arquivo CSV com dados de pessoas e retorna os dados
    
    Args:
        nome_arquivo (str): Nome do arquivo CSV a ser lido
        
    Returns:
        list: Lista de dicionários com os dados das pessoas
    """
    pessoas = []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            
            # Lê todos os registros
            for linha in leitor:
                pessoas.append(linha)
                
        return pessoas
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler arquivo CSV: {e}")
        return []

def exibir_dados_pessoas(pessoas):
    """
    Exibe os dados das pessoas na tela de forma formatada
    
    Args:
        pessoas (list): Lista de dicionários com dados das pessoas
    """
    if not pessoas:
        print("Nenhum dado encontrado.")
        return
    
    print("\n=== DADOS DAS PESSOAS ===")
    print("=" * 60)
    
    # Exibe cabeçalho
    print(f"{'#':<3} {'Nome':<25} {'Idade':<6} {'Cidade':<20}")
    print("-" * 60)
    
    # Exibe cada pessoa
    for i, pessoa in enumerate(pessoas, 1):
        nome = pessoa.get('Nome', 'N/A')
        idade = pessoa.get('Idade', 'N/A')
        cidade = pessoa.get('Cidade', 'N/A')
        
        print(f"{i:<3} {nome:<25} {idade:<6} {cidade:<20}")
    
    print("-" * 60)
    print(f"Total de registros: {len(pessoas)}")

def exibir_estatisticas_pessoas(pessoas):
    """
    Exibe estatísticas sobre os dados das pessoas
    
    Args:
        pessoas (list): Lista de dicionários com dados das pessoas
    """
    if not pessoas:
        return
    
    print("\n=== ESTATÍSTICAS ===")
    print("=" * 40)
    
    # Estatísticas de idade
    idades = []
    cidades = []
    
    for pessoa in pessoas:
        try:
            idade = int(pessoa.get('Idade', 0))
            if idade > 0:
                idades.append(idade)
        except ValueError:
            pass
        
        cidade = pessoa.get('Cidade', '').strip()
        if cidade:
            cidades.append(cidade)
    
    if idades:
        media_idade = sum(idades) / len(idades)
        idade_min = min(idades)
        idade_max = max(idades)
        
        print(f"Idade média: {media_idade:.1f} anos")
        print(f"Idade mínima: {idade_min} anos")
        print(f"Idade máxima: {idade_max} anos")
    
    # Estatísticas de cidades
    if cidades:
        cidades_unicas = set(cidades)
        print(f"Número de cidades diferentes: {len(cidades_unicas)}")
        print(f"Cidades: {', '.join(sorted(cidades_unicas))}")

def filtrar_por_idade(pessoas, idade_min=None, idade_max=None):
    """
    Filtra pessoas por faixa etária
    
    Args:
        pessoas (list): Lista de dicionários com dados das pessoas
        idade_min (int): Idade mínima (opcional)
        idade_max (int): Idade máxima (opcional)
        
    Returns:
        list: Lista filtrada de pessoas
    """
    pessoas_filtradas = []
    
    for pessoa in pessoas:
        try:
            idade = int(pessoa.get('Idade', 0))
            
            # Verifica se a idade está dentro dos critérios
            if idade_min is not None and idade < idade_min:
                continue
            if idade_max is not None and idade > idade_max:
                continue
                
            pessoas_filtradas.append(pessoa)
            
        except ValueError:
            continue
    
    return pessoas_filtradas

def filtrar_por_cidade(pessoas, cidade_busca):
    """
    Filtra pessoas por cidade
    
    Args:
        pessoas (list): Lista de dicionários com dados das pessoas
        cidade_busca (str): Nome da cidade para filtrar
        
    Returns:
        list: Lista filtrada de pessoas
    """
    pessoas_filtradas = []
    
    for pessoa in pessoas:
        cidade = pessoa.get('Cidade', '').strip().lower()
        if cidade_busca.lower() in cidade:
            pessoas_filtradas.append(pessoa)
    
    return pessoas_filtradas

def menu_interativo(pessoas):
    """
    Menu interativo para diferentes visualizações dos dados
    
    Args:
        pessoas (list): Lista de dicionários com dados das pessoas
    """
    while True:
        print("\n=== MENU DE VISUALIZAÇÃO ===")
        print("1. Exibir todos os dados")
        print("2. Exibir estatísticas")
        print("3. Filtrar por idade")
        print("4. Filtrar por cidade")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            exibir_dados_pessoas(pessoas)
            
        elif opcao == "2":
            exibir_estatisticas_pessoas(pessoas)
            
        elif opcao == "3":
            try:
                print("\nFiltro por idade:")
                idade_min = input("Idade mínima (deixe em branco para não filtrar): ").strip()
                idade_max = input("Idade máxima (deixe em branco para não filtrar): ").strip()
                
                idade_min = int(idade_min) if idade_min else None
                idade_max = int(idade_max) if idade_max else None
                
                pessoas_filtradas = filtrar_por_idade(pessoas, idade_min, idade_max)
                
                if pessoas_filtradas:
                    print(f"\nPessoas encontradas (idade entre {idade_min or 'qualquer'} e {idade_max or 'qualquer'}):")
                    exibir_dados_pessoas(pessoas_filtradas)
                else:
                    print("Nenhuma pessoa encontrada com os critérios especificados.")
                    
            except ValueError:
                print("Por favor, digite números válidos para as idades.")
                
        elif opcao == "4":
            cidade_busca = input("Digite o nome da cidade para filtrar: ").strip()
            
            if cidade_busca:
                pessoas_filtradas = filtrar_por_cidade(pessoas, cidade_busca)
                
                if pessoas_filtradas:
                    print(f"\nPessoas encontradas na cidade '{cidade_busca}':")
                    exibir_dados_pessoas(pessoas_filtradas)
                else:
                    print(f"Nenhuma pessoa encontrada na cidade '{cidade_busca}'.")
            else:
                print("Nome da cidade não pode estar vazio.")
                
        elif opcao == "5":
            print("Programa encerrado.")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

def main():
    """
    Função principal do programa
    """
    print("=== LEITOR DE ARQUIVO CSV DE PESSOAS ===\n")
    
    # Nome do arquivo CSV
    nome_arquivo = "pessoas.csv"
    
    # Verifica se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        print("Certifique-se de que o arquivo existe no diretório atual.")
        return
    
    # Lê os dados do arquivo CSV
    print(f"Lendo arquivo '{nome_arquivo}'...")
    pessoas = ler_csv_pessoas(nome_arquivo)
    
    if not pessoas:
        print("Não foi possível carregar os dados.")
        return
    
    print(f"Arquivo carregado com sucesso! {len(pessoas)} registros encontrados.")
    
    # Exibe os dados inicialmente
    exibir_dados_pessoas(pessoas)
    
    # Menu interativo
    menu_interativo(pessoas)

if __name__ == "__main__":
    main()
