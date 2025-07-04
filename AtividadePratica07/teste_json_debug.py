import json
import os

def teste_escrita_json():
    """
    Teste simples para verificar se a escrita JSON está funcionando
    """
    print("🔧 TESTE DE ESCRITA JSON")
    print("="*40)
    
    # Dados de teste simples
    dados_teste = {
        "pessoa": {
            "nome": "Teste Silva",
            "idade": 30,
            "cidade": "Cidade Teste"
        },
        "status": "teste_funcionando"
    }
    
    nome_arquivo = "teste_json.json"
    
    try:
        # Tentativa de escrita
        print(f"📝 Tentando escrever arquivo: {nome_arquivo}")
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_teste, arquivo, ensure_ascii=False, indent=2)
        
        print(f"✅ Arquivo '{nome_arquivo}' criado com sucesso!")
        
        # Verificar se o arquivo foi criado
        if os.path.exists(nome_arquivo):
            tamanho = os.path.getsize(nome_arquivo)
            print(f"📁 Arquivo existe! Tamanho: {tamanho} bytes")
            
            # Tentar ler de volta
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados_lidos = json.load(arquivo)
            
            print("📖 Dados lidos de volta:")
            print(json.dumps(dados_lidos, indent=2, ensure_ascii=False))
            
        else:
            print("❌ Arquivo não foi criado!")
            
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        print(f"Tipo do erro: {type(e).__name__}")

def teste_script_principal():
    """
    Testa o script principal com debug
    """
    print("\n🔧 TESTE DO SCRIPT PRINCIPAL COM DEBUG")
    print("="*50)
    
    # Dados de exemplo
    dados_pessoas = {
        "pessoas": [
            {"nome": "João Debug", "idade": 25, "cidade": "São Paulo"}
        ],
        "total_pessoas": 1,
        "data_criacao": "2025-07-04",
        "versao": "1.0"
    }
    
    nome_arquivo = "debug_pessoas.json"
    
    print(f"📝 Dados a serem escritos:")
    print(json.dumps(dados_pessoas, indent=2, ensure_ascii=False))
    
    try:
        print(f"\n📝 Escrevendo arquivo: {nome_arquivo}")
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_pessoas, arquivo_json, ensure_ascii=False, indent=2)
        
        print(f"✅ Escrita concluída!")
        
        # Verificações
        if os.path.exists(nome_arquivo):
            print(f"✅ Arquivo existe!")
            
            # Ler conteúdo
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
                dados_lidos = json.load(arquivo_json)
            
            print(f"✅ Leitura bem-sucedida!")
            print(f"📊 Pessoas no arquivo: {len(dados_lidos.get('pessoas', []))}")
            
        else:
            print("❌ Arquivo não existe após escrita!")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    teste_escrita_json()
    teste_script_principal()
