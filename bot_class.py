class Bot:
    def __init__(self, movimentos):
        self.movimentos = movimentos
        self.pos_atual = []
        self.chegou_em_objetivo = False

    def calcularDesempenho(self, objetivo):
        # Calculando distancia até o objetivo usando distância manhattan
        return objetivo[0]-self.pos_atual[0] + objetivo[1]-self.pos_atual[1]


    def mover(self, mapa, direcao):
        linha = self.pos_atual[0]
        coluna = self.pos_atual[1]

        if direcao == 'up':
            if linha > 0 and mapa.matriz_casas[linha-1][coluna] == 0:
                self.pos_atual = [linha-1, coluna]

        elif direcao == 'down':
            if linha < mapa.n_linhas-1 and mapa.matriz_casas[linha+1][coluna] == 0:
                self.pos_atual = [linha+1, coluna]

        elif direcao == 'left':
            if coluna > 0 and mapa.matriz_casas[linha][coluna-1] == 0:
                self.pos_atual = [linha, coluna - 1]
        
        elif direcao == 'right':
            if coluna < mapa.n_colunas-1 and mapa.matriz_casas[linha][coluna+1] == 0:
                self.pos_atual = [linha, coluna + 1]
        
        else:
            print("Movimento nao identificado")
        
        # verifica se chegou no objetivo
        if self.pos_atual == mapa.pos_final:
            self.chegou_em_objetivo = True
        
            
        
    def percorrerMapa(self, mapa):

        #inicializa posicao
        self.pos_atual = mapa.pos_inicial

        #traduz vetor de movimentos
        movimento_atual = 0
        while not self.chegou_em_objetivo and movimento_atual < len(self.movimentos) / 2:
            print(f"Movimento atual: {movimento_atual}, Posição atual: {self.pos_atual} - ", end=' ')

            if self.movimentos[movimento_atual*2] == False:
                # movimento vertical
                if self.movimentos[movimento_atual*2+1] == False:
                    # up
                    self.mover(mapa, 'up')
                    print('Up')
                else:
                    # down
                    self.mover(mapa, 'down')
                    print('Down')
            else:
                # movimento horizontal
                if self.movimentos[movimento_atual*2+1] == False:
                    # right
                    self.mover(mapa, 'right')
                    print('Right')
                else:
                    # left
                    self.mover(mapa, 'left')
                    print('Left')
            
            movimento_atual+=1
        

        # Analisa desempenho
        desempenho = self.calcularDesempenho(mapa.pos_final)

        #retornando valores
        return self.movimentos, desempenho


    