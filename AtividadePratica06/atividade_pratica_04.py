import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada ou código inválido.")
            return
        info = dados[chave]
        print(f"Cotação {moeda}/BRL")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Valor máximo: R$ {info['high']}")
        print(f"Valor mínimo: R$ {info['low']}")
        print(f"Data e hora da última atualização: {info['create_date']}")
    except requests.RequestException as e:
        print("Erro ao acessar a API:", e)

codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
consultar_cotacao(codigo_moeda)
