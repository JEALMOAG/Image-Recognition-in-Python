# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:51:38 2024

@author: Jesus Montes
"""
from PIL import Image  # Importa la clase Image de la biblioteca PIL (Pillow)
import numpy as np     # Importa la biblioteca numpy bajo el alias np
import matplotlib.pyplot as plt  # Importa matplotlib.pyplot bajo el alias plt

# Abre la imagen 'y0.4.png' usando PIL (Pillow) y la asigna a la variable i
i = Image.open('y0.4.png')

# Convierte la imagen PIL en una matriz NumPy y la asigna a la variable iar
iar = np.asarray(i)

# Imprime la matriz NumPy que representa la imagen
print(iar)

# Muestra la imagen utilizando matplotlib
plt.imshow(iar)

# Muestra la ventana emergente con la imagen
plt.show()
