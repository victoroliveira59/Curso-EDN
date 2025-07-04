"""
Script de teste para demonstrar a adição de pessoas ao JSON
"""
import json
import os

# Simular a adição de uma pessoa sem input do usuário
def adicionar_pessoa_automatica(nome_arquivo, nome, idade, cidade):
    """
    Adiciona uma pessoa automaticamente (para demonstração)
    """
    try:
        # Lê dados existentes ou cria estrutura inicial
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
        else:
            dados = {
                "pessoas": [],
                "total_pessoas": 0,
                "data_criacao": "2025-07-04",
                "versao": "1.0"
            }
        
        # Adiciona nova pessoa
        nova_pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }
        
        dados['pessoas'].append(nova_pessoa)
        dados['total_pessoas'] = len(dados['pessoas'])
        
        # Salva dados atualizados
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
        
        print(f"✅ Pessoa '{nome}' adicionada com sucesso!")
        print(f"👥 Total de pessoas: {dados['total_pessoas']}")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def mostrar_todas_pessoas(nome_arquivo):
    """
    Mostra todas as pessoas do arquivo
    """
    try:
        if not os.path.exists(nome_arquivo):
            print("❌ Arquivo não existe!")
            return
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        if 'pessoas' not in dados or not dados['pessoas']:
            print("❌ Nenhuma pessoa encontrada!")
            return
        
        print(f"\n👥 PESSOAS NO ARQUIVO ({dados.get('total_pessoas', 0)}):")
        print("="*60)
        
        for i, pessoa in enumerate(dados['pessoas'], 1):
            print(f"{i:2d}. {pessoa['nome']} - {pessoa['idade']} anos - {pessoa['cidade']}")
        
    except Exception as e:
        print(f"❌ Erro ao ler arquivo: {e}")

# Demonstração
print("🧪 TESTE DE ADIÇÃO DE PESSOAS AO JSON")
print("="*50)

nome_arquivo = "teste_pessoas.json"

# Criar arquivo inicial se não existir
if not os.path.exists(nome_arquivo):
    print("📁 Criando arquivo inicial...")
    dados_inicial = {
        "pessoas": [
            {"nome": "João Silva", "idade": 28, "cidade": "São Paulo"},
            {"nome": "Maria Santos", "idade": 35, "cidade": "Rio de Janeiro"}
        ],
        "total_pessoas": 2,
        "data_criacao": "2025-07-04",
        "versao": "1.0"
    }
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados_inicial, arquivo, ensure_ascii=False, indent=2)
    print("✅ Arquivo inicial criado!")

# Mostrar pessoas atuais
print("\n📖 Pessoas antes da adição:")
mostrar_todas_pessoas(nome_arquivo)

# Adicionar novas pessoas
print("\n➕ Adicionando novas pessoas...")
adicionar_pessoa_automatica(nome_arquivo, "Ana Costa", 29, "Brasília")
adicionar_pessoa_automatica(nome_arquivo, "Pedro Oliveira", 42, "Salvador")
adicionar_pessoa_automatica(nome_arquivo, "Carla Mendes", 31, "Fortaleza")

# Mostrar pessoas após adição
print("\n📖 Pessoas após adição:")
mostrar_todas_pessoas(nome_arquivo)

print(f"\n✅ Teste concluído! Arquivo '{nome_arquivo}' criado/atualizado.")
print("💡 Para usar interativamente, execute: python atividade_pratica_04_novo.py")
