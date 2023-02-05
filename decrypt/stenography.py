import cv2
import numpy as np
import os
import binascii
import sys
from itertools import combinations 


def encoding(imagePath, dataToEncrypt):
    imageData    = cv2.imread(imagePath)
    numBytesPic  = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3))

    numLocations = 10

    splitData  = list(split(dataToEncrypt, numLocations))   # split data into 10 parts
    temp = []
    for d in splitData:
        temp.append(''.join(format(ord(i), '08b') for i in d))
    splitData = temp
    for i,d in enumerate(splitData):
        splitData[i] = d + '00000000'
    splitMergedData = ''.join(splitData)
    maxDataLen = max([len(d) for d in splitData])

    maxNumBits       = int(np.ceil(np.log2(numBytesPic)))
    numBytesReserved = numLocations * (8 + maxNumBits)
    numBytesUsable   = numBytesPic-numBytesReserved
    indices = np.random.randint(0, numBytesUsable, numLocations) #[location1, location2];
    indices = np.sort(indices)
    for c in range(numLocations):
        for i,idx in enumerate(indices):
            if i == len(indices)-1:
                break
            if indices[i+1] - idx < maxDataLen:
                indices[i] = idx - maxDataLen
                if indices[i] < 0:
                    indices[i] = 0
                    indices[i+1] = maxDataLen
    
    indicesEnds = indices.copy()
    idxs2       = np.array([], dtype=int)
    for i,idx in enumerate(indices):
        idxs2 = np.append(idxs2, np.arange(idx, idx+len(splitData[i])))
    idxs2   = np.array(idxs2, dtype=int)
    indices = idxs2

    maxNum  = len(format(numBytesPic, 'b'))
    allIndicesEnds = ''
    for i,num in enumerate(indicesEnds):
        num = format(num, 'b')
        num = num.zfill(maxNum)
        allIndicesEnds += num

    imgDatFlat = imageData.flatten()
    for i,indx in enumerate(indices):
        rgb = imgDatFlat[indx]
        rgb = format(rgb, '08b')
        rgb = rgb[:-1] + str(splitMergedData[i])
        # dataIdx += 1
        imgDatFlat[indx] = int(rgb, 2)

    
    curRGBIdx = 0
    imgDatFlat = imgDatFlat[::-1]
    for i,rgb in enumerate(imgDatFlat):
        rgb = format(rgb, '08b')
        rgb = rgb[:-1] + str(allIndicesEnds[curRGBIdx])
        curRGBIdx += 1
        imgDatFlat[i] = int(rgb, 2)
        if curRGBIdx == len(allIndicesEnds):
            break
    imgDatFlat = imgDatFlat[::-1]
    imageData  = imgDatFlat.reshape(imageData.shape)
          
    cv2.imwrite('decrypt/stockimageEncrypted.png', imageData)
    return


def decode(imagePath):
    imageData   = cv2.imread(imagePath)
    numBytesPic = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3))
    numLocations = 10
    maxNum = len(format(numBytesPic, 'b'))
    reverseData = imageData.flatten()[::-1]
    locations = getLocations(reverseData, numLocations, maxNum)

    flattened = imageData.flatten()
    

    binaryData  = ''
    unencrypted = ''
    for k,loc in enumerate(locations):
        curSearchArea = flattened[loc:]
        for rgb in curSearchArea:
            rgb   = format(rgb, '08b')
            rgb   = rgb[-1]
            binaryData += rgb
            if len(binaryData) == 8:
                newchar      = chr(int(binaryData, 2))
                if newchar == '\0':
                    binaryData   = ''
                    break
                unencrypted += newchar
                binaryData   = ''
    return unencrypted


def getLocations(reverseData, numLocations, maxNum):
    locations     = []
    locationCount = 0
    temp          = ''
    for k, rgb in enumerate(reverseData):
        rgb   = format(rgb, '08b')
        rgb   = rgb[-1]
        temp += rgb
        if len(temp) == maxNum:
            locations.append(int(temp, 2))
            locationCount += 1
            temp = ''
            if locationCount == numLocations:
                return locations
    return locations


def split(a, n):
    k, m = divmod(len(a), n)
    splitted = (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
    return splitted


def findPairs(lst, K, n):
    return [pair for pair in combinations(lst, n) if sum(pair) == K]





if __name__ == '__main__':
    encoding('decrypt/stockimage.png', 'abasdjksadsadisahdij ajidas idasi disudh ash sahdsaih diuasid sahdui asidhasiu dhsaih iuahu ahdiuahd uisdhiu sahiuashuishac')
    print('encoded')
    decoded = decode('decrypt/stockimageEncrypted.png')
    print('decoded',decoded)

