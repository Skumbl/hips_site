from hips_hack.stenography import encode, decode

# encode(imagePath='/Users/trumandewalch/Downloads/IMG_0632.JPG', dataToEncrypt='hello!', outputImagePath='/Users/trumandewalch/Downloads/IMG_0632_encrypted.JPG')
message = decode(imagePath='/Users/trumandewalch/Downloads/IMG_0632_encrypted.png')
print(message)


# encode(imagePath='decrypt/stockimage.png', dataToEncrypt='hello!', outputImagePath='decrypt/stockimage_encrypted.png')
# message = decode(imagePath='decrypt/stockimage_encrypted.png')
# print(message)
