import texte
import image
import chiffrement
import os

while True:
    os.system('cls||clear')
    print("------------------------")
    print("Choisissez une action:")
    print("(0): Chiffrer un texte")
    print("(1): Chiffrer une image")
    print("(2): Déchiffrer un texte")
    print("(3): Déchiffrer une image")
    print("\n")
   
    nb = input("Entrez le chiffre correspondant au fichier souhaité: ")
      
    if (nb == ("0" or "")):
        texte.start()
    elif (nb == "1"):
        image.start()
    elif (nb == "3"):
        priv = chiffrement.clePrivee(
          chiffrement.demanderNombre("p"),
          chiffrement.demanderNombre("q"),
          chiffrement.demanderNombre("e")
        );
        
        image.dechiffrerImage(priv)
    else:
        print("Action incomprise!")
    
    input("Appuyez sur Entrée pour continuer...")
