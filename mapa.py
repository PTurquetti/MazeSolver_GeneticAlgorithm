class Map:
    def __init__(self, n_linhas, n_colunas, casas, pos_inicial, pos_final):
        self.n_linhas = n_linhas
        self.n_colunas = n_colunas
        self.matriz_casas = casas
        self.pos_inicial = pos_inicial
        self.pos_final = pos_final
    

    def printMap(self):
        print("Esse é o mapa")
        for i in range(self.n_linhas):
            for j in range(self.n_colunas):
                print(self.matriz_casas[i][j], end=' ')
            print()
    
    #def definirCasas(self)

