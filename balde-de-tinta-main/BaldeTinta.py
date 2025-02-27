import numpy as np

class BaldeTinta:
    # https://www.geeksforgeeks.org/flood-fill-algorithm/
    # peguei daqui
        
    @staticmethod
    def DFS_Pilha(matriz:np.ndarray[int],linha:int,coluna:int,novaCor:int) -> None:
        totalLinhas:int = len(matriz)
        colunas:int = len(matriz[0])
        
        corAntiga:int = matriz[linha][coluna]
        
        pilha:list[tuple[int, int]] = [(linha, coluna)]
        
        # explora as posições embaixo, em cima, direita e esquerda
        vizinhosDe4:list[tuple[int,int]] = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # vizinhosDe8 = [(1, 0), (-1, 0), (0, 1), (0, -1),  # Horizontais e verticais
        #                (1, 1), (-1, -1), (-1, 1), (1, -1)]  # Diagonais
        
        matriz[linha][coluna] = novaCor
        
        while pilha:
            x, y = pilha.pop()
            
            for direcaoX,direcaoY in vizinhosDe4:
                nX:int = x + direcaoX
                nY:int = y + direcaoY
                
                if 0 <= nX < totalLinhas and 0 <= nY < colunas and matriz[nX][nY] == corAntiga:
                    matriz[nX][nY] = novaCor
                    pilha.append((nX,nY))
        
        return matriz