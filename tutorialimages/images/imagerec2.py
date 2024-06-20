
"""
Created on Sun Jun 16 15:50:20 2024

@author: Jesus Montes
"""

from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
from functools import reduce

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray.copy()
    
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    
    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0:4] = [255, 255, 255, 255]
            else:
                eachPix[0:4] = [0, 0, 0, 255]
    return newAr

# Load images
i1 = Image.open("0.1.png")
iar1 = np.array(i1)

i2 = Image.open("y0.4.png")
iar2 = np.array(i2)

i3 = Image.open("y0.5.png")
iar3 = np.array(i3)

i4 = Image.open("sentdex.png")
iar4 = np.array(i4)

# Apply threshold function
iar3 = threshold(iar3)
iar2 = threshold(iar2)
iar4 = threshold(iar4)
# Plotting images
fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(iar1)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()

