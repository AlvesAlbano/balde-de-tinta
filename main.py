from BaldeTinta import BaldeTinta
from Matriz import Matriz

import numpy as np
import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar os pacotes. Verifique o arquivo requirements.txt.")

def main():
    install_requirements()

    arquivo = "data/UNIFOR_grayscale.txt"
    
    matriz = Matriz(arquivo)
    
    linha = 0
    coluna = 0
    nova_cor = 8
    
    print("Antes:")
    matriz.print_matriz()
    
    matriz.matriz = BaldeTinta.DFS_Pilha(matriz.matriz, linha, coluna, nova_cor)
    print("Depois:")
    matriz.print_matriz()         
                         
if __name__ == '__main__':
    main()