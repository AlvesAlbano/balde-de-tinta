# Converte uma imagem para grayscale e exporta TXT

from PIL import Image
import numpy as np

img = Image.open('imagens/UNIFOR_logo_.png')
img = img.convert("L")

arr = np.asarray(img)
np.savetxt('imagens/UNIFOR_logo_grayscale.txt', arr, fmt='%d')

img.save('imagens/UNIFOR_logo_grayscale.jpg')
img.show()