from hips_hack.stenography import encode, decode

encode(imagePath='/Users/trumandewalch/Hackathon/decrypt/stockimage.png', dataToEncrypt='hello!', output_image='/Users/trumandewalch/Hackathon/decrypt/stockimage_encrypted.png')
message = decode(imagePath='/Users/trumandewalch/Hackathon/decrypt/stockimage_encrypted.png')
print(message)
# encode(imagePath='/Users/trumandewalch/Hackathon/decrypt/stockimage.png', output_image='/Users/trumandewalch/Hackathon/decrypt/stockimage_encrypted.png')
