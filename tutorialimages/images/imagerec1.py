# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:50:20 2024

@author: Jesus Montes
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

# Definición de la función threshold
def threshold(imageArray):
    blance = []
    newAr = imageArray
    
    for eachRow in imageArray:
        for eachPix in eachRow:
            print(eachPix)
            time.sleep(2)

# Cargar imágenes y convertirlas en matrices NumPy
i1 = Image.open("0.1.png")
iar1 = np.array(i1)

i2 = Image.open("y0.4.png")
iar2 = np.array(i2)

i3 = Image.open("y0.5.png")
iar3 = np.array(i3)

i4 = Image.open("sentdex.png")
iar4 = np.array(i4)

# Llamar a la función threshold con una de las imágenes
threshold(iar3)

# Configurar subtramas y mostrar las imágenes usando matplotlib
fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3) 
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()

