<from PIL import Image
from chiffrement import chiffrer, dechiffrer, choixCle, clePublique

import os

def confirm_choice(msg):
    confirm = input(msg + " -> [O] Oui [N] Non ").lower()
    
    if confirm != 'o' and confirm != 'n':
        print("\n Option invalide. Entrez une option valide.")
        return confirm_choice() 
    
    print(confirm)
    return confirm

"""
Déchiffre une image choisie dans le dossier /output
Paramètres: cle -> clé privée
"""
def dechiffrerImage(cle):
  while True:
    try:
      print("Choisissez une image à déchiffrer dans le répertoire:")

      files = os.listdir("./output")

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
  # Lecture du fichier
  img = Image.open("./output/" + path, 'r')
  img = img.convert('RGB')

  print("Lecture terminée")
  print("Déchiffrement en cours...");

  # Boucle pour chaque pixel
  width, height = img.size

  for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        print(r, g, b)
        
        r = dechiffrer(r, cle)
        g = dechiffrer(g, cle)
        b = dechiffrer(b, cle)

        print(r, g, b)

        r = r % 256
        g = g % 256
        b = b % 256
        
        print(r, g, b)

        img.putpixel((x, y), (r, g, b))

  # Fin du déchiffrement
  print('Déchiffrement terminé')

  filename, file_extension = os.path.splitext(path)

  img.save("./decrypted/" + filename + file_extension)

  print('Fichier écrit')  
  input("Appuyez sur Entrée pour continuer...")

"""
Chiffre une image choisie dans le dossier /images
Paramètres: cle -> clé publique
"""
def chiffrerImage(cle):
  while True:
    try:
      print("Choisissez une image à chiffrer dans le répertoire:")

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

  # Lecture du fichier
  img = Image.open("./images/" + path, 'r')
  img = img.convert('RGB')

  print("Lecture terminée")
  print("Chiffrement en cours...");

  # Boucle pour chaque pixel
  width, height = img.size

  for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        
        r = chiffrer(r, cle)
        g = chiffrer(g, cle)
        b = chiffrer(b, cle)

        r = r % 256
        g = g % 256
        b = b % 256

        img.putpixel((x, y), (r, g, b))

  # Fin du chiffrement
  print('Chiffrement terminé')

  filename, file_extension = os.path.splitext(path)

  img.save("./output/" + filename + file_extension)
  print('Ecriture terminée')  

def start():
  p, q, e = choixCle(100, 1000)
  pub = clePublique(p, q, e)

  print("P: {0} | Q: {1} | E: {2}".format(p, q, e))
  print("Clé publique: " + repr(pub))

  chiffrerImage(pub)