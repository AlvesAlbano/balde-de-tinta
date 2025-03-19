# Converte uma imagem para grayscale e exporta TXT

from PIL import Image
import numpy as np

# Lê a imagem no caminho relativo especificado
img = Image.open('imagens/UNIFOR_logo_.png')
# Usa o argumento L para acinzentar a imagem 
img = img.convert("L")

# Armazena o matriz da imagem acinzentada 
arr = np.asarray(img)
# Salva a imagem como um .txt no caminho relativo especificado, usa %d para formatar os valores para inteiros
np.savetxt('imagens/UNIFOR_logo_grayscale.txt', arr, fmt='%d')

img.save('imagens/UNIFOR_logo_grayscale.jpg')
img.show()