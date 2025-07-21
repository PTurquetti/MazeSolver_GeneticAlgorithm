import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from gerenciador import algGenetico

#estabelecer parametros
n_bots = 24
n_movimentos = 30
#n_geracoes = 1000
max_geracoes = 5000
taxa_mutacao = 0.02

#algGenetico(n_bots, n_movimentos, max_geracoes, taxa_mutacao, mapa)


def gerar_mapa(nlinhas, ncolunas, janelaConfig):
    """Gera o mapa com dimensões especificadas e implementa clique para alterar células."""
    try:
        linhas = int(nlinhas.get())
        colunas = int(ncolunas.get())
        if linhas <= 0 or colunas <= 0:
            raise ValueError
    except ValueError:
        print("Erro. Por favor, insira valores numéricos positivos para linhas e colunas.")
        return

    # Oculta a janela principal
    janelaConfig.withdraw()

    # Cria a janela do mapa
    janelaMapa = tk.Tk()
    janelaMapa.title(f'Mapa {linhas} x {colunas}')

    # Inicializa a matriz
    matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    def alterar_cor(label, i, j):
        """Altera a cor do quadrado e atualiza a matriz."""
        if matriz[i][j] == 0:  # Se for 0, mude para preto
            label.config(bg='black')
            matriz[i][j] = 1
        else:  # Se for 1, volte para branco
            label.config(bg='white')
            matriz[i][j] = 0

        #print(f"Matriz atualizada: {matriz}")  # Exibe a matriz atualizada no terminal

    for i in range(linhas):
        for j in range(colunas):
            # Cria um Label para cada célula e associa um clique para alterar a cor
            label = tk.Label(janelaMapa, width=6, height=3, bg='white')
            label.grid(row=i, column=j, padx=1, pady=1)
            label.bind("<Button-1>", lambda e, lbl=label, x=i, y=j: alterar_cor(lbl, x, y))

    def fechar_mapa():
        """Fecha a janela do mapa e reabre a janela principal."""
        janelaConfig.deiconify()
        janelaMapa.destroy()
    

    # Botão para iniciar o algoritmo
    botaoIniciar = tk.Button(janelaMapa, text='Iniciar', command=lambda: algGenetico(n_bots, n_movimentos, max_geracoes, taxa_mutacao, linhas, colunas, matriz))
    botaoIniciar.grid(row=linhas + 1, column=int(colunas / 2), pady=10)

    # Configura o evento de fechamento da janela do mapa
    janelaMapa.protocol("WM_DELETE_WINDOW", fechar_mapa)

    janelaMapa.mainloop()

def iniciar_janela_principal():
    """Inicia a janela principal para configurar o mapa."""
    janelaConfig = tk.Tk()
    janelaConfig.title('Algoritmo Genético - Solução de Labirinto')

    nlinhas = tk.Entry(janelaConfig, width=10)
    nlinhas.grid(row=0, column=0, padx=10, pady=10)

    textoLinhas = tk.Label(janelaConfig, text=' Linhas')
    textoLinhas.grid(row=0, column=1, padx=3, pady=10)

    textoX = tk.Label(janelaConfig, text='   X   ')
    textoX.grid(row=0, column=2, padx=10, pady=10)

    ncolunas = tk.Entry(janelaConfig, width=10)
    ncolunas.grid(row=0, column=3, padx=10, pady=10)

    textoColunas = tk.Label(janelaConfig, text=' Colunas')
    textoColunas.grid(row=0, column=4, padx=3, pady=10)

    botaoGerar = tk.Button(
        janelaConfig,
        text='Gerar Mapa',
        command=lambda: gerar_mapa(nlinhas, ncolunas, janelaConfig),
        background='Blue'
    )
    botaoGerar.grid(row=1, column=2, padx=10, pady=10)

    janelaConfig.mainloop()

iniciar_janela_principal()
