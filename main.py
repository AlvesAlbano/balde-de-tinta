from BaldeTinta import BaldeTinta

import numpy as np
import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar os pacotes. Verifique o arquivo requirements.txt.")

if __name__ == '__main__':
    install_requirements()
    
    matrizTeste:np.ndarray[int] = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ])
    
    linha:int = 0
    coluna:int = 1
    novaCor:int = 999
    
    print(f"Antes: \n{matrizTeste}")
    
    print(f"Depois: \n{BaldeTinta.DFS_Pilha(matrizTeste,linha,coluna,novaCor)}")