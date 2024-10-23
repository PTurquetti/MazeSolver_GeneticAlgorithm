import random
import numpy as np
from mapa import Map
from bot_class import Bot


#funcao crossover
def crossoverSimples(A, B, x):
    A_new = np.append(A[:x], B[x:])
    B_new = np.append(B[:x], A[x:])
    return A_new, B_new

def mutacao(movimento, taxa_mutacao):
    for i in range(len(movimento)):
        if random.random() < taxa_mutacao:
            movimento[i] = not movimento[i]
    
    return movimento

def algGenetico(n_bots, n_movimentos, max_geracoes, taxa_mutacao):

    bots = []
    resultados = []

    #criar mapa
    nlinhas = 5
    ncolunas = 10
    matriz_mapa = [
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
                ]
    pos_inicial = [0, 0]
    pos_final = [4, 9]

    mapa = Map(nlinhas, ncolunas, matriz_mapa, pos_inicial, pos_final)
    mapa.printMap(matriz=None)


    #criar vetor de movimento da primeira geração
    for i in range(n_bots):
        movimentos = [random.choice([True,False]) for _ in range(n_movimentos * 2)]
        #print(movimentos)
        botzinho = Bot(movimentos)
        bots.append(botzinho)

    a = 0
    tem_solucao = False
    while a < max_geracoes:
    #for a in range(n_geracoes):
        #colocar geração para rodar e receber arrays de movimento e desempenho de cada bot da geracao
        botzinho = 0
        for botzinho in bots:
            movimentos, desempenho = botzinho.percorrerMapa(mapa)
            resultados.append((movimentos, desempenho))


        #ordenar arrays de movimento de acordo com o desempenho
        resultados.sort(key=lambda x:x[1])

        #printando resultados
        print(f"Geração {a+1} - Melhor Resultado: {resultados[0][1]}")

        if resultados[0][1] == 0:
            tem_solucao = True
            mapa.imprimeCaminho(resultados[0][0])
            break


        bots.clear()
        for x in range(int(n_bots / 2)):
            mov_filho1, mov_filho2 = crossoverSimples(resultados[x][0], resultados[x+1][0], n_movimentos)

            #print(mov_filho1, mov_filho2)

            botzinho1 = Bot(mutacao(mov_filho1, taxa_mutacao))
            botzinho2 = Bot(mutacao(mov_filho2, taxa_mutacao))

            bots.append(botzinho1)
            bots.append(botzinho2)

        resultados.clear()
        a += 1

    if(not tem_solucao):
        print('Solução não encontrada')


