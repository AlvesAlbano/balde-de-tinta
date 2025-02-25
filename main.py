import numpy as np
from BuscaLargura import BuscaLargura

import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar os pacotes. Verifique o arquivo requirements.txt.")

if __name__ == '__main__':
    install_requirements()
    matrizTest:np.ndarray[int] = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ])
    
    BuscaLargura.BFS(matrizTest)
    print("teste")