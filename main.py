import random
from mapa import Map
from bot_class import Bot

#estabelecer parametros
n_bots = 1
n_movimentos = 10
n_geracoes = 10
bots = []
resultados = []



#criar mapa
nlinhas = 5
ncolunas = 5
matriz_mapa = [
               [0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0],
               [0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0]
            ]
pos_inicial = [0, 0]
pos_final = [4, 4]

mapa = Map(nlinhas, ncolunas, matriz_mapa, pos_inicial, pos_final)
mapa.printMap()


#criar vetor de movimento da primeira geração
for i in range(n_bots):
    movimentos = [random.choice([True,False]) for _ in range(n_movimentos * 2)]
    botzinho = Bot(movimentos)
    bots.append(botzinho)

#colocar geração para rodar
for botzinho in bots:
    movimentos, desempenho = botzinho.percorrerMapa(mapa)
    resultados.append((movimentos, desempenho))


#printando resultados
print("Resultados")
for resultado in resultados:
    print(resultado)

#receber arrays de movimento e desempenho de cada bot da geracao

#ordenar arrays de movimento de acordo com o desempenho

#fazer crossover

#carregar nova geracao
# -- retornar para etapa "colocar geracao para rodar"

