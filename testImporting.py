from hips_hack.stenography import encode, decode

encode(imagePath='/Users/trumandewalch/Hackathon/decrypt/stockimage.png', dataToEncrypt='hello!', outputImagePath='/Users/trumandewalch/Hackathon/decrypt/stockimage_encrypted.png')
message = decode(imagePath='/Users/trumandewalch/Hackathon/decrypt/stockimage_encrypted.png')
print(message)


encode(imagePath='decrypt/stockimage.png', dataToEncrypt='hello!', outputImagePath='decrypt/stockimage_encrypted.png')
message = decode(imagePath='decrypt/stockimage_encrypted.png')
print(message)
