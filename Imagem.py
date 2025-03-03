import cv2
import numpy as np
from BaldeTinta import BaldeTinta
from PIL import Image

class Imagem:
    nomeJanela: str = "imagem"
    
    def __init__(self, caminhoArquivo: str):
        self.caminhoArquivo = caminhoArquivo
        self.matrizTexto = np.loadtxt(caminhoArquivo)
        # self.matrizTexto = self.converteImagemEmMatriz()
        self.matrizImagem = np.uint8(self.matrizTexto)
    
    def manipularImagem(self, event, x, y, flags, param):
        if event == cv2.EVENT_FLAG_LBUTTON:
            cv2.putText(self.matrizImagem, f"[X:{x}, Y:{y}]", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif event == cv2.EVENT_FLAG_RBUTTON:
            imagemEditada = BaldeTinta.DFS_Pilha(self.matrizTexto,x,y,0)
            self.matrizImagem = np.uint8(imagemEditada)
        
        cv2.imshow(self.nomeJanela,self.matrizImagem)
        cv2.waitKey(1)

            
    def verImagem(self) -> None:
        # largura, altura = self.retornarDimensoes()
        
        cv2.imshow(self.nomeJanela, self.matrizImagem)
        # cv2.resizeWindow(self.nomeJanela,largura,altura)
        cv2.setMouseCallback(self.nomeJanela, self.manipularImagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def retornarDimensoes(self):
        imagem = Image.open(self.caminhoArquivo)
        largura, altura = imagem.size
        
        return largura, altura
    
    def converteImagemEmMatriz(self):
        matrizImagem = Image.open(self.caminhoArquivo)
        
        return np.array(matrizImagem, dtype=np.uint8).copy()