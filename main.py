from BaldeTinta import BaldeTinta
from Matriz import Matriz
from Imagem import Imagem

import subprocess
import sys
import cv2
import numpy as np

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar os pacotes. Verifique o arquivo requirements.txt.")

def main():
    # install_requirements()

    caminhoArquivo:str = "imagens/UNIFOR_grayscale.txt"
    # caminhoArquivo:str = "imagens/imagem_teste.txt"
    #caminhoArquivo:str = "imagens/UNIFOR_grayscale.png"
    
    imagem:Imagem = Imagem(caminhoArquivo)
    # print(imagem.converteImagemEmMatriz())
    imagem.verImagem()
    
    
    # linha:int = 10
    # coluna:int = 7
    # nova_cor:int = 8
    
    # matrizImagem = np.loadtxt(caminhoArquivo)
    # print(f"Antes \n{np.uint8(matrizImagem)}")
    # print(f"Depois \n{np.uint8(BaldeTinta.FloodFill(matrizImagem,linha,coluna,nova_cor))}")
    
    # novaImagem = BaldeTinta.DFS_Pilha(matrizImagem,linha,coluna,nova_cor)
    
    # imagem:Imagem = Imagem("teste.txt")
    # imagem.verImagem()
    
    # Imagem.verImagem(novaImagem)
    
    # Imagem.verImagem(caminhoArquivo)
    
    # arquivo:str = "data/imagem_teste.txt"
    # matriz:Matriz = Matriz(arquivo)
    
    # print("Antes:")
    # matriz.print_matriz()
    
    # matriz.matriz = BaldeTinta.DFS_Pilha(matriz.matriz, linha, coluna, nova_cor)
    # print("Depois:")
    # matriz.print_matriz()         
                         
if __name__ == '__main__':
    main()