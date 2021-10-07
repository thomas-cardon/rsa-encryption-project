print("Lecture de l'image")

fileInput = open("./images/64x64.png", 'rb')

image = fileInput.read()
fileInput.close()

# Conversion en bytearray pour chiffrer + facilement  les données numériques
image = bytearray(image)

print("Lecture terminée")
print(image.hex())

# Chiffrement
encrypted = image
# Fin du chiffrement
print('Chiffrement terminé')

fileOutput = open("./output.png", 'wb')
fileOutput.write(encrypted)
fileOutput.close()

print('Fichier écrit')