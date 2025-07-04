import json
import os

def criar_dados_pessoas_json():
    """
    Cria dados de exemplo de pessoas para salvar em JSON
    
    Returns:
        dict: Dicionário com dados das pessoas
    """
    dados_pessoas = {
        "pessoas": [
            {
                "nome": "João Silva",
                "idade": 28,
                "cidade": "São Paulo"
            },
            {
                "nome": "Maria Santos",
                "idade": 35,
                "cidade": "Rio de Janeiro"
            },
            {
                "nome": "Pedro Oliveira",
                "idade": 22,
                "cidade": "Belo Horizonte"
            },
            {
                "nome": "Ana Costa",
                "idade": 41,
                "cidade": "Brasília"
            },
            {
                "nome": "Carlos Souza",
                "idade": 33,
                "cidade": "Salvador"
            }
        ],
        "total_pessoas": 5,
        "data_criacao": "2025-07-04",
        "versao": "1.0"
    }
    return dados_pessoas

def escrever_json(nome_arquivo, dados):
    """
    Escreve dados em um arquivo JSON
    
    Args:
        nome_arquivo (str): Nome do arquivo JSON a ser criado
        dados (dict): Dados a serem escritos no arquivo
    """
    try:
        print(f"🔧 DEBUG: Tentando escrever arquivo: {nome_arquivo}")
        print(f"🔧 DEBUG: Diretório atual: {os.getcwd()}")
        print(f"🔧 DEBUG: Tipo dos dados: {type(dados)}")
        print(f"🔧 DEBUG: Dados a serem escritos: {dados}")
        
        # Verificar se o diretório é acessível
        caminho_completo = os.path.abspath(nome_arquivo)
        print(f"🔧 DEBUG: Caminho completo: {caminho_completo}")
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            # Escreve os dados com indentação para melhor legibilidade
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=2)
        
        # Verificar se o arquivo foi realmente criado
        if os.path.exists(nome_arquivo):
            tamanho = os.path.getsize(nome_arquivo)
            print(f"✅ Arquivo '{nome_arquivo}' criado com sucesso!")
            print(f"📊 Total de pessoas salvas: {dados.get('total_pessoas', 0)}")
            print(f"📁 Tamanho do arquivo: {tamanho} bytes")
        else:
            print(f"❌ ERRO: Arquivo não foi criado mesmo sem exceção!")
        
    except PermissionError:
        print(f"❌ Erro de permissão ao escrever arquivo JSON: {nome_arquivo}")
        print("💡 Verifique se você tem permissão para escrever neste diretório")
    except Exception as e:
        print(f"❌ Erro ao escrever arquivo JSON: {e}")
        print(f"🔧 DEBUG: Tipo do erro: {type(e).__name__}")

def ler_json(nome_arquivo):
    """
    Lê dados de um arquivo JSON
    
    Args:
        nome_arquivo (str): Nome do arquivo JSON a ser lido
        
    Returns:
        dict: Dados lidos do arquivo JSON ou None se houver erro
    """
    try:
        print(f"🔧 DEBUG: Tentando ler arquivo: {nome_arquivo}")
        print(f"🔧 DEBUG: Arquivo existe? {os.path.exists(nome_arquivo)}")
        
        if os.path.exists(nome_arquivo):
            tamanho = os.path.getsize(nome_arquivo)
            print(f"🔧 DEBUG: Tamanho do arquivo: {tamanho} bytes")
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
        
        print(f"✅ Arquivo '{nome_arquivo}' lido com sucesso!")
        print(f"🔧 DEBUG: Tipo dos dados lidos: {type(dados)}")
        return dados
        
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{nome_arquivo}' não encontrado.")
        print(f"🔧 DEBUG: Diretório atual: {os.getcwd()}")
        print(f"🔧 DEBUG: Arquivos no diretório:")
        try:
            for arquivo in os.listdir('.'):
                if arquivo.endswith('.json'):
                    print(f"   - {arquivo}")
        except:
            print("   (Não foi possível listar arquivos)")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao decodificar JSON: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro ao ler arquivo JSON: {e}")
        print(f"🔧 DEBUG: Tipo do erro: {type(e).__name__}")
        return None

def exibir_dados_pessoas(dados):
    """
    Exibe os dados das pessoas de forma formatada
    
    Args:
        dados (dict): Dados das pessoas lidos do JSON
    """
    if not dados or 'pessoas' not in dados:
        print("❌ Nenhum dado de pessoa encontrado.")
        return
    
    print(f"\n{'='*60}")
    print(f"📋 DADOS DAS PESSOAS")
    print(f"{'='*60}")
    
    # Exibe informações gerais
    print(f"📅 Data de criação: {dados.get('data_criacao', 'N/A')}")
    print(f"🔢 Versão: {dados.get('versao', 'N/A')}")
    print(f"👥 Total de pessoas: {dados.get('total_pessoas', len(dados['pessoas']))}")
    print(f"{'='*60}")
    
    # Exibe dados de cada pessoa
    for i, pessoa in enumerate(dados['pessoas'], 1):
        print(f"{i:2d}. 👤 Nome: {pessoa.get('nome', 'N/A'):<20}")
        print(f"     🎂 Idade: {pessoa.get('idade', 'N/A'):<3} anos")
        print(f"     🏙️ Cidade: {pessoa.get('cidade', 'N/A')}")
        print(f"     {'-'*40}")

def adicionar_pessoa_json(nome_arquivo):
    """
    Adiciona uma nova pessoa ao arquivo JSON
    
    Args:
        nome_arquivo (str): Nome do arquivo JSON
    """
    try:
        # Lê dados existentes
        print(f"📖 Carregando dados do arquivo '{nome_arquivo}'...")
        dados = ler_json(nome_arquivo)
        if dados is None:
            print("❌ Não foi possível ler o arquivo para adicionar nova pessoa.")
            return False
        
        print(f"\n{'='*50}")
        print("➕ ADICIONAR NOVA PESSOA")
        print(f"{'='*50}")
        
        # Mostra quantas pessoas já existem
        total_atual = len(dados.get('pessoas', []))
        print(f"👥 Pessoas atualmente no arquivo: {total_atual}")
        print(f"{'='*50}")
        
        # Coleta dados da nova pessoa
        print("📝 Digite os dados da nova pessoa:")
        
        while True:
            nome = input("👤 Nome completo: ").strip()
            if nome:
                break
            print("❌ Nome não pode estar vazio. Tente novamente.")
        
        while True:
            try:
                idade_str = input("🎂 Idade: ").strip()
                idade = int(idade_str)
                if idade < 0:
                    print("❌ Idade deve ser um número positivo.")
                    continue
                elif idade > 150:
                    print("❌ Idade parece muito alta. Tem certeza? (Digite novamente para confirmar)")
                    continue
                break
            except ValueError:
                print("❌ Por favor, digite um número válido para a idade.")
        
        while True:
            cidade = input("🏙️ Cidade: ").strip()
            if cidade:
                break
            print("❌ Cidade não pode estar vazia. Tente novamente.")
        
        # Mostra resumo antes de salvar
        print(f"\n{'='*50}")
        print("📋 RESUMO DA NOVA PESSOA:")
        print(f"👤 Nome: {nome}")
        print(f"🎂 Idade: {idade} anos")
        print(f"🏙️ Cidade: {cidade}")
        print(f"{'='*50}")
        
        confirmacao = input("✅ Confirma a adição desta pessoa? (s/n): ").strip().lower()
        
        if confirmacao not in ['s', 'sim', 'y', 'yes']:
            print("❌ Operação cancelada pelo usuário.")
            return False
        
        # Adiciona nova pessoa
        nova_pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }
        
        # Garante que a lista de pessoas existe
        if 'pessoas' not in dados:
            dados['pessoas'] = []
        
        dados['pessoas'].append(nova_pessoa)
        dados['total_pessoas'] = len(dados['pessoas'])
        
        # Atualiza data de modificação (opcional)
        from datetime import datetime
        dados['ultima_modificacao'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Salva os dados atualizados
        print(f"\n💾 Salvando dados no arquivo...")
        escrever_json(nome_arquivo, dados)
        
        print(f"\n🎉 SUCESSO!")
        print(f"✅ Pessoa '{nome}' adicionada com sucesso!")
        print(f"👥 Total de pessoas agora: {len(dados['pessoas'])}")
        
        return True
        
    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário.")
        return False
    except Exception as e:
        print(f"❌ Erro ao adicionar pessoa: {e}")
        print(f"🔧 DEBUG: Tipo do erro: {type(e).__name__}")
        return False

def menu_principal():
    """
    Menu principal para gerenciar pessoas no arquivo JSON
    """
    nome_arquivo = "pessoas_exemplo.json"
    
    print("🐍 SISTEMA DE GERENCIAMENTO DE PESSOAS - JSON")
    print("="*60)
    
    while True:
        print(f"\n{'='*40}")
        print("📋 MENU PRINCIPAL")
        print(f"{'='*40}")
        print("1. 📖 Ler e exibir todas as pessoas")
        print("2. ➕ Adicionar nova pessoa")
        print("3. ✍️  Criar arquivo inicial (se não existir)")
        print("4. 📄 Mostrar conteúdo bruto do JSON")
        print("5. 📊 Mostrar estatísticas")
        print("0. 🚪 Sair")
        print(f"{'='*40}")
        
        try:
            opcao = input("👉 Escolha uma opção: ").strip()
            
            if opcao == '1':
                # Ler e exibir pessoas
                dados = ler_json(nome_arquivo)
                if dados:
                    exibir_dados_pessoas(dados)
                else:
                    print("❌ Não foi possível ler o arquivo. Use a opção 3 para criar um arquivo inicial.")
            
            elif opcao == '2':
                # Adicionar nova pessoa
                if not os.path.exists(nome_arquivo):
                    print("❌ Arquivo não existe. Use a opção 3 para criar um arquivo inicial primeiro.")
                else:
                    adicionar_pessoa_json(nome_arquivo)
            
            elif opcao == '3':
                # Criar arquivo inicial
                print("✍️ Criando arquivo inicial com dados de exemplo...")
                dados_exemplo = criar_dados_pessoas_json()
                escrever_json(nome_arquivo, dados_exemplo)
            
            elif opcao == '4':
                # Mostrar conteúdo bruto
                if os.path.exists(nome_arquivo):
                    print(f"\n📄 CONTEÚDO BRUTO DO ARQUIVO '{nome_arquivo}':")
                    print("="*60)
                    try:
                        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                            conteudo = arquivo.read()
                            print(conteudo)
                    except Exception as e:
                        print(f"❌ Erro ao ler arquivo: {e}")
                else:
                    print("❌ Arquivo não existe. Use a opção 3 para criar.")
            
            elif opcao == '5':
                # Mostrar estatísticas
                dados = ler_json(nome_arquivo)
                if dados and 'pessoas' in dados:
                    pessoas = dados['pessoas']
                    print(f"\n📊 ESTATÍSTICAS:")
                    print(f"👥 Total de pessoas: {len(pessoas)}")
                    
                    if pessoas:
                        idades = [p.get('idade', 0) for p in pessoas]
                        print(f"🎂 Idade média: {sum(idades)/len(idades):.1f} anos")
                        print(f"🎂 Idade mínima: {min(idades)} anos")
                        print(f"🎂 Idade máxima: {max(idades)} anos")
                        
                        cidades = [p.get('cidade', '') for p in pessoas]
                        cidades_unicas = list(set(cidades))
                        print(f"🏙️ Cidades diferentes: {len(cidades_unicas)}")
                        print(f"🏙️ Cidades: {', '.join(cidades_unicas)}")
                else:
                    print("❌ Não há dados para mostrar estatísticas.")
            
            elif opcao == '0':
                print("👋 Encerrando programa...")
                break
            
            else:
                print("❌ Opção inválida. Tente novamente.")
        
        except KeyboardInterrupt:
            print("\n👋 Programa interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

def demonstracao_simples():
    """
    Função de demonstração simples para testar o código
    """
    print("🐍 DEMONSTRAÇÃO: LEITURA E ESCRITA DE ARQUIVO JSON")
    print("="*60)
    
    # Criar dados de exemplo
    print("\n1. Criando dados de exemplo...")
    dados = criar_dados_pessoas_json()
    
    # Escrever no arquivo JSON
    print("\n2. Escrevendo dados no arquivo JSON...")
    nome_arquivo = "pessoas_exemplo.json"
    escrever_json(nome_arquivo, dados)
    
    # Ler do arquivo JSON
    print("\n3. Lendo dados do arquivo JSON...")
    dados_lidos = ler_json(nome_arquivo)
    
    # Exibir os dados
    if dados_lidos:
        print("\n4. Exibindo dados lidos:")
        exibir_dados_pessoas(dados_lidos)
    
    print(f"\n✅ Demonstração concluída! Arquivo '{nome_arquivo}' criado com sucesso.")
    print("\n💡 Para usar o sistema interativo, execute: menu_principal()")

if __name__ == "__main__":
    # Perguntar se quer demonstração ou menu interativo
    print("🐍 SISTEMA DE GERENCIAMENTO DE PESSOAS EM JSON")
    print("="*60)
    print("1. 🚀 Menu interativo (recomendado)")
    print("2. 🧪 Demonstração simples")
    
    try:
        escolha = input("👉 Escolha uma opção (1 ou 2): ").strip()
        
        if escolha == '1':
            menu_principal()
        elif escolha == '2':
            demonstracao_simples()
        else:
            print("Opção inválida. Executando menu interativo...")
            menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma interrompido.")
    except:
        print("Executando menu interativo...")
        menu_principal()
