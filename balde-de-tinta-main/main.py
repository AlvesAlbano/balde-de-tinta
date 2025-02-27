from BaldeTinta import BaldeTinta

import numpy as np
import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar os pacotes. Verifique o arquivo requirements.txt.")

def get_matrix_length():
    with open("data/UNIFOR_sample.txt", "r", encoding="utf-8") as archive:
        line = archive.readline()
        no_spaces = line.replace(" ", "")

        return len(no_spaces.strip())

def get_matrix_height():
    count = 0

    for line in archive:
        count += 1
        
    return count

if __name__ == '__main__':
    install_requirements()
    
    # matrizTeste:np.ndarray[int] = np.array([
    #     [0, 1, 1, 0],
    #     [1, 0, 1, 1],
    #     [1, 1, 0, 1],
    #     [0, 1, 1, 0]
    # ])

    matrizTeste = []

    with open("data/UNIFOR_sample.txt", "r", encoding="utf-8") as arquivo:
        for teste in arquivo:
            print(teste.strip())
    
    linha:int = 0
    coluna:int = 1
    novaCor:int = 9
    
    print(f"Antes: \n{matrizTeste}")
    
    print(f"Depois: \n{BaldeTinta.DFS_Pilha(matrizTeste,linha,coluna,novaCor)}")