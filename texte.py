from chiffrement import chiffrer, dechiffrer, choixCle, clePublique, clePrivee
from utils import confirm

def chiffrerTexte(cle, texte = "Hello World !"):
  print("--- [ Chiffrement de texte ] ---")  
  print("Texte à chiffrer: " + texte)

  tableau = []
  for char in texte:
    tableau.append(chiffrer(ord(char), cle))

  texteChiffre = ''
  for ascii in tableau:
    texteChiffre += chr(ascii)
  
  print("Texte chiffré: \"" + texteChiffre + '"\n\n')
  return texteChiffre

def dechiffrerTexte(cle, texte):
  print("--- [ Déchiffrement de texte ] ---")
  print("Texte à déchiffrer: " + texte)

  tableau = []
  for char in texte:
    tableau.append(dechiffrer(ord(char), cle))

  texteDechiffre = ''
  for ascii in tableau:
    texteDechiffre += chr(ascii)
  
  print("Texte déchiffré: \"" + texteDechiffre + '"\n\n')

def start():
  p, q, e = choixCle(20, 127)
  pub = clePublique(p, q, e)
  priv = clePrivee(p, q, e)

  print("P: {0} | Q: {1} | E: {2}".format(p, q, e))
  print("Clé publique: " + repr(pub))

  texte = chiffrerTexte(pub, input("Que voulez-vous chiffrer? "))

  if (confirm("Voulez-vous laisser le programme déchiffrer le texte à l'aide des clés privées déjà générées?\n") == True):
    dechiffrerTexte(priv, texte)