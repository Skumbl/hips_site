import cv2
import numpy as np
import os
import binascii
import sys
from itertools import combinations 
from time import sleep


def encoding(imagePath, dataToEncrypt):
    imageData   = cv2.imread(imagePath)
    numBitsPic  = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3 * 8))
    numBytesPic = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3))
    binaryData  = ''.join(format(ord(i), '08b') for i in dataToEncrypt)
    numBitsData = len(binaryData)

    numLocations     = 10

    splitData = list(split(binaryData, numLocations))   # split data into 10 parts
    for i,d in enumerate(splitData):
        splitData[i] = d + '00000000'
    splitMergedData = ''.join(splitData)
    print('splitMergedData: ', splitMergedData)
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
    idxs2 = np.array([], dtype=int)
    for i,idx in enumerate(indices):
        idxs2 = np.append(idxs2, np.arange(idx, idx+len(splitData[i])))
    idxs2 = np.array(idxs2, dtype=int)
    indices = idxs2
    print('indices: ', indices)




    maxNum  = len(format(numBytesPic, 'b'))
    allIndicesEnds = ''
    for i,num in enumerate(indicesEnds):
        num = format(num, 'b')
        num = num.zfill(maxNum) + '00000000'
        allIndicesEnds += num
    print(allIndicesEnds)

    #[location (as an rgb index), how many bits to write in that location]

    dataIdx = 0
    imgDatFlat = imageData.flatten()
    for i,rgb in enumerate(imgDatFlat):
        if i in indices:
            rgb = format(rgb, '08b')
            rgb = rgb[:-1] + str(splitMergedData[dataIdx])
            dataIdx += 1
            imgDatFlat[i] = int(rgb, 2)
            if dataIdx == len(splitData):
                break

    
    curRGBIdx = 0
    imageData = imageData[::-1]
    for i,rgb in enumerate(imgDatFlat):
        rgb = format(rgb, '08b')
        rgb = rgb[:-1] + str(allIndicesEnds[curRGBIdx])
        curRGBIdx += 1
        imgDatFlat[i] = int(rgb, 2)
        if curRGBIdx == len(allIndicesEnds):
            break
    imageData = imageData[::-1]
    imageData = imgDatFlat.reshape(imageData.shape)
          
    cv2.imwrite('decrypt/stockimageEncrypted.png', imageData)
    return


def decode(imagePath):
    imageData = cv2.imread(imagePath)
    imageData = imageData.flatten()
    imageData = imageData[::-1]

    loc = ''
    for i,rgb in enumerate(imageData):
        sleep(0.1)
        rgb = format(rgb, '08b')
        loc += rgb[-1]
        


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


# Python3 program to find all pairs in
# a list of integers with given sum

def findPairs(lst, K, numNums):
    return [pair for pair in combinations(lst, numNums) if sum(pair) == K]





def invert(h):
    if h == -1: return []  # -1 gets coerced to -2 so no value has hash -1
    if h < 0:
        sign = -1
        h = -h
    else:
        sign = 1
    M = sys.float_info.mant_dig - 1  # = 52 = Bits available for mantissa
    E = (sys.float_info.max_exp - sys.float_info.min_exp + 1)  # = 1023 = bias
    B = sys.float_info.radix  # = 2, base of the floating point values
    P = sys.hash_info.modulus  # = 2^61 - 1 = the prime used as hash modulus
    if not (0 <= h == int(h) < P):
        return []
    for e in range((E + 1) * 2):
        # Want m such that (B^M + m) * B^(e-M-E) = h mod P
        m = (h * B**(M+E-e) - B**M) % P
        if m >= B**M: continue  # Happens with probability (1-B**M/P)
        f = (B**M + m) * B**(e-M-E)
        if f == int(f): continue  # We'll see this later as an integer
        assert hash(f) == h
        yield sign * f
    # Special values if any
    if h == sys.hash_info.inf:
        yield sign * float('inf')
    if h == sys.hash_info.nan:
        yield float('nan')
    # Now the integers
    k = 0
    while True:
        yield sign * (h + k * P)
        k += 1
    


if __name__ == '__main__':
    encoding('decrypt/stockimage.png', 'hello world')
    print(decode('decrypt/stockimageEncrypted.png'))
