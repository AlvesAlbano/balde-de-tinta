# Converte uma imagem para PB e exporta TXT

from PIL import Image
import numpy as np

img = Image.open('imgs/exemplo_2.png')
img = img.convert('1')

arr = np.asarray(img)
np.savetxt('data/UNIFOR_sample.txt', arr, fmt='%d')

img.save('imgs/exemplo_2.png')
img.show()