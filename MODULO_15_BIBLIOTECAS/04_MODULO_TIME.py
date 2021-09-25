import time


# Segundos (?)
print(time.time())

# Data completa (do momento atual)
print(time.ctime())

tempo_inicial = time.time()
for I in range(1000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(f'Levou  {duracao:.2f} Tempo para Rodar')

# Para esperar até concluir execução de processos:
print('Start Now')
time.sleep(4)
print(f'Concluido em {time.ctime()}')

#Data Atual:
atual = time.gmtime()
# Digite .tm após o objéto e veja todas as opções que você pode adquirir
print(f'Dia Atual: {atual.tm_yday}  do Ano {atual.tm_year}') # 19/09/2021== Dia 263 do ano de 2021

local = atual.tm_zone
print(local)
