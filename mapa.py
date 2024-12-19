import tkinter as tk
from tkinter import ttk
from tkinter import *

class Map:
    def __init__(self, n_linhas, n_colunas, casas, pos_inicial, pos_final):
        self.n_linhas = n_linhas
        self.n_colunas = n_colunas
        self.matriz_casas = casas
        self.pos_inicial = pos_inicial
        self.pos_final = pos_final
    

    def printMap(self, matriz):
        if matriz == None:
            matriz = self.matriz_casas
        
        print("Esse é o mapa")
        for i in range(self.n_linhas):
            for j in range(self.n_colunas):
                print(matriz[i][j], end=' ')
            print()

        # Cria a janela do mapa
        janelaSolucao = tk.Tk()
        janelaSolucao.title(f'Solução do Mapa:')

        # Inicializa a matriz
        

        def definirBackground(matriz, i, j):
            if matriz[i][j] == 0:
                return 'white'
            elif matriz[i][j] == 1:
                return 'black'
            elif matriz[i][j] == 2:
                return 'red'
            

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                # Cria um Label para cada célula e associa um clique para alterar a cor
                label = tk.Label(janelaSolucao, width=6, height=3, bg=definirBackground(matriz, i, j))
                label.grid(row=i, column=j, padx=1, pady=1)
                

    

    def imprimeCaminho(self, movimento):
    
        sequencia_movimentos=[]
        pos_atual = self.pos_inicial  # Faz uma cópia para evitar alterar a posição inicial
        matriz_resultado = self.matriz_casas
        matriz_resultado[self.pos_inicial[0]][self.pos_inicial[1]] = 2

        for i in range(len(movimento) // 2):  # Dividindo o comprimento da lista por 2
            linha = pos_atual[0]
            coluna = pos_atual[1]
            moveu = False

            # Movimento vertical ou horizontal baseado nos valores de movimento
            if movimento[i * 2] == False:
                # Movimento vertical
                if movimento[i * 2 + 1] == False:
                    # Para cima (up)
                    if linha > 0 and matriz_resultado[linha-1][coluna] != 1:
                        nova_pos = [linha - 1, coluna]
                        sequencia_movimentos.append('Up')
                        moveu = True
                else:
                    # Para baixo (down)
                    if linha < self.n_linhas-1 and matriz_resultado[linha+1][coluna] != 1:
                        nova_pos = [linha + 1, coluna]
                        sequencia_movimentos.append('Down')
                        moveu = True
            else:
                # Movimento horizontal
                if movimento[i * 2 + 1] == False:
                    # Para a direita (right)
                    if coluna < self.n_colunas-1 and matriz_resultado[linha][coluna+1] != 1:
                        nova_pos = [linha, coluna + 1]
                        sequencia_movimentos.append('Right')
                        moveu = True
                else:
                    # Para a esquerda (left)
                    if coluna > 0 and matriz_resultado[linha][coluna-1] != 1:
                        nova_pos = [linha, coluna - 1]
                        sequencia_movimentos.append('Left')
                        moveu = True

            # se posicao dentro do limite do mapa
            if moveu:
                if 0 <= nova_pos[0] < self.n_linhas and 0 <= nova_pos[1] < self.n_colunas:
                    pos_atual = nova_pos  # Atualiza a posição
                    matriz_resultado[pos_atual[0]][pos_atual[1]] = 2 
                else:
                    # passou limite do mapa, deu erro
                    print("Movimento fora dos limites do mapa: ", nova_pos)
                    break  
            
            if pos_atual == self.pos_final:
                break

        self.printMap(matriz_resultado)
        print(sequencia_movimentos)
   
    

