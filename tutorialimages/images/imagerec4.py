# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:24:39 2024

@author: Jesus Montes
"""

from PIL import Image
import numpy as np
from collections import Counter

def createExamples():
    with open('numArEx.txt', 'a') as numbersArrayExamples:
        numbersWeHave = range(0, 10)
        versionsWeHave = range(1, 10)
        for eachNum in numbersWeHave:
            for eachVer in versionsWeHave:
                print(f"{eachNum}.{eachVer}")
                imgFilePath = f"{eachNum}.{eachVer}.png"
                ei = Image.open(imgFilePath).convert('RGB')  # Convertir a RGB
                eiar = np.array(ei)
                eiar1 = str(eiar.tolist())
                lineToWrite = f"{eachNum}::{eiar1}\n"
                numbersArrayExamples.write(lineToWrite)

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray.copy()

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = np.mean(eachPix[:3])
            balanceAr.append(avgNum)
    balance = np.mean(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if np.mean(eachPix[:3]) > balance:
                eachPix[0:3] = [255, 255, 255]
            else:
                eachPix[0:3] = [0, 0, 0]
    return newAr

def whatNumIsThis(filePath):
    matchedAr = []
    with open('numArEx.txt', 'r') as f:
        loadExamps = f.read().split('\n')
    
    i = Image.open(filePath).convert('RGB')  # Convert to RGB
    iar = np.array(i)
    iarl = str(iar.tolist())
    
    inQuestion = np.array(eval(iarl))

    # Check and convert to RGB if necessary
    if inQuestion.shape[2] == 4:  # If image has 4 channels (RGBA), convert to RGB
        inQuestion = inQuestion[:, :, :3]

    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = np.array(eval(splitEx[1]))

            # Ensure both arrays have the same shape (only compare RGB channels)
            if currentAr.shape[2] == inQuestion.shape[2]:
                matched_pixels = np.sum(currentAr == inQuestion)
                total_pixels = currentAr.size
                match_ratio = matched_pixels / total_pixels

                if match_ratio > 0.9:  # Assuming 90% similarity threshold
                    matchedAr.append(int(currentNum))
            else:
                print(f"Discrepancia de forma: {currentAr.shape} vs {inQuestion.shape}")

    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    return x
