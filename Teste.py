from datetime import datetime
import logging
from tqdm import tqdm
import time

# # Exemplo de loop simples
# for i in tqdm(range(10), desc="Processando valores", unit="qtd", unit_scale=True, position=0):
#     time.sleep(0.5)  # Simulando algum trabalho

#     # Calculando o tempo restante aproximado
#     tempo_decorrido = (i + 1) * 0.5
#     tempo_restante = (10 - (i + 1)) * 0.5

#     # Formatando o tempo decorrido e o tempo restante
#     tempo_decorrido_str = time.strftime(
#         "%H:%M:%S", time.gmtime(tempo_decorrido))
#     tempo_restante_str = time.strftime("%H:%M:%S", time.gmtime(tempo_restante))

#     # Atualizando a descrição na barra de progresso
#     tqdm.write(f"Tempo decorrido: {tempo_decorrido_str}, Tempo restante: {
#                tempo_restante_str}")


# Inicialização de variáveis para calcular a média
soma_tempo = 0


def tempo():
    # Exemplo de loop com descrição personalizada para tempo decorrido, tempo restante e média
    for i in tqdm(range(100), desc="Tempo", position=0):
        time.sleep(0.5)  # Simulando algum trabalho

        # Calculando o tempo decorrido
        tempo_decorrido = (i + 1) * 0.5
        soma_tempo += tempo_decorrido

        # Calculando o tempo restante aproximado
        tempo_restante = (10 - (i + 1)) * 0.5

        # Calculando a média até o ponto atual
        media_tempo = soma_tempo / (i + 1)

        # Formatando os tempos em horas:minutos:segundos
        tempo_decorrido_str = time.strftime(
            "%H:%M:%S", time.gmtime(tempo_decorrido))
        tempo_restante_str = time.strftime(
            "%H:%M:%S", time.gmtime(tempo_restante))
        media_tempo_str = time.strftime("%H:%M:%S", time.gmtime(media_tempo))

        # Atualizando a descrição na barra de progresso
        tqdm.write(f"Tempo decorrido: {tempo_decorrido_str}, Tempo restante: {
            tempo_restante_str}, Média: {media_tempo_str}")
    return ()

# from tqdm import tqdm
# import time

# # Exemplo de loop com descrição personalizada para tempo decorrido, tempo restante e média
# for i in tqdm(range(100000), desc="Tempo", position=0):
#     time.sleep(0.5)  # Simulando algum trabalho

#     # Calculando o tempo decorrido
#     tempo_decorrido = (i + 1) * 0.5

#     # Calculando o tempo restante aproximado
#     tempo_restante = (10 - (i + 1)) * 0.5

#     # Formatando os tempos em horas:minutos:segundos
#     tempo_decorrido_str = time.strftime(
#         "%H:%M:%S", time.gmtime(tempo_decorrido))
#     tempo_restante_str = time.strftime("%H:%M:%S", time.gmtime(tempo_restante))

#     # Construindo a descrição para a barra de progresso
#     descricao = f"{tempo_decorrido_str}<{tempo_restante_str}, {i + 1}/{10}"

#     # Atualizando a descrição na barra de progresso
#     tqdm.write(descricao, end='\r')


# print(tempo())


# Obtendo a data e hora atual
data_hora_atual = datetime.now()

# Formatando a data e hora no formato desejado (DDMMYYYY)
data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y-T%H")

# Caminho do arquivo de log com a data e hora atual
caminho_arquivo_log = f"./Log/Log{
    data_hora_formatada}.log"

# Configurando o logger para escrever no arquivo de log
logging.basicConfig(filename=caminho_arquivo_log, level=logging.DEBUG, encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplo de uso do logger
logging.info("Este é um registro de exemplo.")
