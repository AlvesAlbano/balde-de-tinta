import cv2
import numpy as np
from BaldeTinta import BaldeTinta
from utils.graph import Graph

class Imagem:
    nomeJanela: str = "Editor de Imagens"
    
    def __init__(self, caminhoArquivo: str):
        # Leitura da matriz e conversão para grafo
        self.caminhoArquivo = caminhoArquivo
        self.matrizTexto = np.loadtxt(caminhoArquivo)
        self.matrizImagem = np.uint8(self.matrizTexto) 
        self.grafo = self.matrizParaGrafo(self.matrizImagem)

    def manipularImagem(self, event, x, y, flags, param):
        # Manipula a imagem com o clique do mouse
        if event == cv2.EVENT_LBUTTONDOWN:
            cor_inicial = self.matrizImagem[y, x]  # Pega a cor inicial do pixel clicado
            print(f"Cor inicial no ponto ({x}, {y}): {cor_inicial}")

            # Realiza a operação de preenchimento (DFS no grafo)
            v_inicial = y * len(self.matrizImagem[0]) + x
            grafo_modificado = BaldeTinta.FloodFill(self.grafo, v_inicial, 0)  # 0 = nova cor (preto)
            
            self.atualizaImagem(grafo_modificado)

            print(f"Cor final no ponto ({x}, {y}): {self.matrizImagem[y, x]}")

        # Exibe a imagem
        cv2.imshow(self.nomeJanela, self.matrizImagem)
        cv2.waitKey(1)

    def atualizaImagem(self, grafo):
        # Converte o grafo de volta para a matriz de imagem
        rows, cols = self.matrizImagem.shape
        for i in range(rows):
            for j in range(cols):
                vertice = i * cols + j
                self.matrizImagem[i, j] = grafo.get_color(vertice)  # Atualiza com a nova cor

    def verImagem(self) -> None:     
        cv2.imshow(self.nomeJanela, self.matrizImagem)
        cv2.setMouseCallback(self.nomeJanela, self.manipularImagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def matrizParaGrafo(self, matriz):
        # Chama o método matrix_to_graph() da classe Graph
        print("Construindo grafo...")
        rows, cols = len(matriz), len(matriz[0])
        grafo = Graph(rows * cols)
        grafo.matrix_to_graph(matriz)
        print("Grafo construído.")
        return grafo