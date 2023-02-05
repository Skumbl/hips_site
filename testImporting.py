from hips_hack.stenography import encode, decode

# encode(imagePath='/Users/trumandewalch/Downloads/testing.jpeg', dataToEncrypt='hello!', outputImagePath='/Users/trumandewalch/Downloads/testing_encrypted.png')
message = decode(imagePath='/Users/trumandewalch/Downloads/testing_encrypted.png')
print(message)


# encode(imagePath='decrypt/stockimage.png', dataToEncrypt='hello!', outputImagePath='decrypt/stockimage_encrypted.png')
# message = decode(imagePath='decrypt/stockimage_encrypted.png')
# print(message)
