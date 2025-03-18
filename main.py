from Imagem import Imagem

import subprocess
import sys


def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Falha ao instalar os pacotes. Verifique o arquivo requirements.txt.")

def main():
    # install_requirements()

    caminhoArquivo:str = "imagens/UNIFOR_logo_grayscale.txt"
    
    imagem:Imagem = Imagem(caminhoArquivo)
    imagem.verImagem()
       
                         
if __name__ == '__main__':
    main()