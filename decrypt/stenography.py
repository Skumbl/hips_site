import cv2
import numpy as np
import os
import binascii
import sys
from itertools import combinations 


def encoding(imagePath, dataToEncrypt):
    imageData   = cv2.imread(imagePath)
    numBitsPic  = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3 * 8))
    numBytesPic = int(np.floor(imageData.shape[0] * imageData.shape[1] * 3))
    binaryData  = ''.join(format(ord(i), '08b') for i in dataToEncrypt) + '00000000'
    numBitsData = len(binaryData)

    numLocations     = 10
    maxNumBits       = int(np.ceil(np.log2(numBytesPic)))
    numBytesReserved = numLocations * (8 + maxNumBits)
    numBytesUsable   = numBytesPic-numBytesReserved
    indices = np.random.randint(0, numBytesUsable, numLocations) #[location1, location2];
    #[num of bits to write for location1, num of bits to write for location2]
    #[actual bits(text) for location1, actual bits(text) for location2]

    indices = np.sort(indices)

    maxNum  = len(format(numBytesPic, 'b'))
    for i,num in enumerate(indices):
        num = format(num, 'b')
        num = num.zfill(maxNum)

    #[location (as an rgb index), how many bits to write in that location]

    curDataIdx = 0 #the current index to pull data from on the splitData
    currRunIdx = 0 #As if it were a flattened array, the index of the rgb value
    currLocationIdx = 0 #which location are we currently using?
    #write = False;
    for i,row in enumerate(imageData):
        for j,pixel in enumerate(row):
            # convert RGB values to binary format
            for k,rgb in enumerate(pixel):
                if currRunIdx == indices[currLocationIdx] + curDataIdx:
                    rgb         = format(rgb, '08b')
                    rgb         = rgb[:-1] + str(splitData[currLocationIdx][curDataIdx])
                    curDataIdx += 1
                    imageData[i][j][k] = int(rgb, 2)
                    if curDataIdx == len(splitData[currLocationIdx]):
                        curDataIdx = 0
                        currLocationIdx += 1
                # if curDataIdx < len(binaryData):
                #     rgb         = format(rgb, '08b')
                #     rgb         = rgb[:-1] + str(binaryData[curDataIdx])
                #     curDataIdx += 1
                #     # convert rgb back to int
                #     imageData[i][j][k] = int(rgb, 2)
                currRunIdx += 1
    
    curRGBIdx  = 0
    imageData = imageData[::-1, ::-1, ::-1]
    print('imageData: ', imageData)
    # for i,row in enumerate(imageData):
    #     for j,pixel in enumerate(row):
    #         # convert RGB values to binary format
    #         for k,rgb in enumerate(pixel):

    #             curRGBIdx += 1
                
    # cv2.imwrite('decrypt/stockimageEncrypted.png', imageData)
    return


def decode(imagePath):
    imageData   = cv2.imread(imagePath)

    curDataIdx  = 0
    binaryData  = ''
    unencrypted = ''
    for i,row in enumerate(imageData):
        # print('Encoding row: ', i, ' of ', imageData.shape[0])
        for j,pixel in enumerate(row):
            # convert RGB values to binary format
            for k,rgb in enumerate(pixel):
                # if curDataIdx < len(binaryData):
                rgb         = format(rgb, '08b')
                rgb         = rgb[-1]
                binaryData += rgb
                if len(binaryData) == 8:
                    newchar = chr(int(binaryData, 2))
                    unencrypted += newchar
                    binaryData   = ''
                    if newchar == '\0':
                        return unencrypted
                curDataIdx += 1

    # print('unencrypted: ', unencrypted)
    # return unencrypted



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
    # print(decode('decrypt/stockimageEncrypted.png'))
