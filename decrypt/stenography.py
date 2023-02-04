import cv2
import numpy as np
import os
import binascii
import sys
from itertools import combinations 


def encoding(imagePath, dataToEncrypt):
    imageData   = cv2.imread(imagePath)
    numBitsPic  = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3/8))
    binaryData  = ''.join(format(ord(i), '08b') for i in dataToEncrypt)
    numBitsData = len(binaryData)
    places      = np.random.randint(0, numBitsPic, numBitsData)
    places      = np.sort(places)
    placesHash  = hash(np.sum(places))

    num=0
    for n in invert(placesHash):
        num += 1
        if num > 25: break
    reverseHash = hash(n)
    print(reverseHash)
    print(placesHash)


    # def findPairs(lst, K, N): 
    #     return [pair for pair in combinations(lst, N) if sum(pair) == K] 
    
    print(np.arange(0,numBitsPic))
    # import sys
    # print(sys.getrecursionlimit())
    sys.setrecursionlimit(10000)
    findPairs(np.arange(0,numBitsPic), reverseHash, numBitsData)

    curDataIdx  = 0
    convertedLSBs = []
    for i,row in enumerate(imageData):
        print('Encoding row: ', i, ' of ', imageData.shape[0])
        for j,pixel in enumerate(row):
            # convert RGB values to binary format
            for k,rgb in enumerate(pixel):
                if curDataIdx < len(binaryData):
                    rgb = format(rgb, '08b')
                    convertedLSBs.append(rgb[-1])
                    rgb = rgb[:-1] + str(binaryData[curDataIdx])
                    curDataIdx += 1
                    pixel[k] = int(rgb, 2)
    print('Converted LSBs: ', convertedLSBs)
    cv2.imwrite('encrypt/stockimage.png', imageData)
    return


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
    # print(decode('decrypt/stockimage.png'))
