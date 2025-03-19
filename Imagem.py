import cv2
import numpy as np
from BaldeTinta import BaldeTinta
from utils.graph import Graph

class Imagem:
    nomeJanela: str = "Editor de Imagens"
    
    def __init__(self, caminhoArquivo: str):
        # @Leitura da matriz e conversão para grafo
        self.caminhoArquivo = caminhoArquivo
        # Lê a o .txt da matriz armazenada no caminhoArquivo
        self.matrizTexto = np.loadtxt(caminhoArquivo)
        # Codifica o .txt usando uint8 para ajustar os valores para inteiros, evitando que a imagem fique transparente
        self.matrizImagem = np.uint8(self.matrizTexto) 
        # Transforma a matriz em grafo
        self.grafo = self.matrizParaGrafo(self.matrizImagem)

    def manipularImagem(self, event, coluna, linha, flags, param):
        # Manipula a imagem com o clique do mouse
        if event == cv2.EVENT_LBUTTONDOWN:
            cor_inicial = self.matrizImagem[linha, coluna]  # Pega a cor inicial do pixel clicado
            print(f"Cor inicial no ponto ({linha}, {coluna}): {cor_inicial}")

            # @Realiza a operação de preenchimento (DFS no grafo)
            # converte a posição da linha e coluna em um indice linear
            v_inicial = linha * len(self.matrizImagem[0]) + coluna
            # preenche todos o vertices conectados ao v_inicial por 0 (preto)
            grafo_modificado = BaldeTinta.FloodFill(self.grafo, v_inicial, 0)
            
            self.atualizaImagem(grafo_modificado)

            print(f"Cor final no ponto ({linha}, {coluna}): {self.matrizImagem[linha, coluna]}")

        # Exibe a imagem
        cv2.imshow(self.nomeJanela, self.matrizImagem)
        cv2.waitKey(1)

    def atualizaImagem(self, grafo):
        # Converte o grafo de volta para a matriz de imagem
        # usa o .shape para retornar o valor de linhas e colunas da imagem
        rows, cols = self.matrizImagem.shape
        
        # um loop duplo que percorre cada pixel da imagem
        for i in range(rows):
            for j in range(cols):
                vertice = i * cols + j # calcula o indice do vertice correspondente do grafo
                self.matrizImagem[i, j] = grafo.get_color(vertice)  # Atualiza com a nova cor

    def verImagem(self):     
        cv2.imshow(self.nomeJanela, self.matrizImagem)
        cv2.setMouseCallback(self.nomeJanela, self.manipularImagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def matrizParaGrafo(self, matriz):
        # Chama o método matrix_to_graph() da classe Graph
        print("Construindo grafo...")
        rows, cols = len(matriz), len(matriz[0]) # obtem os valores da linhas e colunas da matriz
        grafo = Graph(rows * cols) # cria um grafo de linha*coluna vertices
        grafo.matrix_to_graph(matriz) # constroi o grafo a partir da matriz
        print("Grafo construído.")
        return grafo