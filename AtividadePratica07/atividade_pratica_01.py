import numpy as np

def ler_log_e_calcular_tempos(log_path):
    # Lista para armazenar os tempos de execução
    tempos_execucao = []

    # Abrir o arquivo de log
    with open(log_path, 'r') as arquivo_log:
        for linha in arquivo_log:
            # Suponha que cada linha tenha o tempo de execução no formato "Tempo: X segundos"
            # Vamos procurar por uma string "Tempo: " na linha
            if "Tempo:" in linha:
                # Encontrando a substring "Tempo: " e pegando o valor numérico após ela
                try:
                    tempo_str = linha.split("Tempo:")[1].strip()  # Pega o que vem depois de "Tempo: "
                    tempo_float = float(tempo_str.split()[0])  # Converte para float
                    tempos_execucao.append(tempo_float)
                except ValueError:
                    print(f"Erro ao converter tempo na linha: {linha}")

    # Verificando se a lista de tempos não está vazia
    if tempos_execucao:
        # Calculando a média e o desvio padrão
        media = np.mean(tempos_execucao)
        desvio_padrao = np.std(tempos_execucao)

        return media, desvio_padrao
    else:
        print("Nenhum tempo de execução encontrado no arquivo.")
        return None, None

# Exemplo de uso
log_path = "log.txt"
media, desvio_padrao = ler_log_e_calcular_tempos(log_path)

if media is not None:
    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
