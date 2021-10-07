import os

print("Choisissez une image dans le répertoire:")

path = ""

def confirm_choice(msg):
    confirm = input(msg + " -> [O] Oui [N] Non ").lower()
    
    if confirm != 'o' and confirm != 'n':
        print("\n Option invalide. Entrez une option valide.")
        return confirm_choice() 
    
    print(confirm)
    return confirm

while True:
  try:
    print("Choisissez une image dans le répertoire:")

    files = os.listdir("./images")

    for idx, val in enumerate(files):
      print("({0}) {1}".format(idx, val))

    nb = int(input("Entrez le chiffre correspondant au fichier souhaité:"))

    if nb > len(files):
      raise Exception()
    else:
      path = files[nb]
      break;
  except ValueError:
      os.system('cls||clear')
      print("/!\ Cette valeur n'est pas un chiffre valide.\n")

print("Lecture fichier: {0}".format(path))
fileInput = open("./images/" + path, 'rb')

image = fileInput.read()
fileInput.close()

print("Lecture terminée")

if confirm_choice("Souhaitez vous visualiser l'image?"):
  print(image.hex())

# Conversion en bytearray pour chiffrer + facilement  les données numériques
image = bytearray(image)

# Chiffrement
encrypted = image
# Fin du chiffrement
print('Chiffrement terminé')

fileOutput = open("./output.png", 'wb')
fileOutput.write(encrypted)
fileOutput.close()

print('Fichier écrit')