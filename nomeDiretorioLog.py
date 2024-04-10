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
