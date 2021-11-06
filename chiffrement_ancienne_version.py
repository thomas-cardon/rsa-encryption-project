import random

"""
    estNombrePremier(num)
    -> Vérifie si un chiffre est premier
"""
def estNombrePremier(num):
    if num > 1:

        # Itération de 2 à n / 2
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

"""
    pgcd(a,b)
    -> Donne le plus grand commun diviseur de deux nombre entiers non nuls
"""
def pgcd(a,b):
    print("--- Calcul PGCD ---");
    while b:
        a, b = b, a % b
        print(a, b)
    
    print("--- Fin Calcul PGCD ---")
    return a

"""
    premiersentreeux(a,b)
    -> Vérifie si a et b sont premiers entre eux
"""
def premiersentreeux(a,b):
    return pgcd(a,b) == 1;

"""
    euclideEtendu(a,b)
    -> Calcule le PGCD ainsi qu'un des couples de coefficients de Bezout, c'est-à-dire deux entiers u et v tels que au + bv = PGCD(a, b)
"""
def euclideEtendu(a, b):
    # L'algorithme s'arrête quand on trouve 0
    if a == 0:
        return b, 0, 1
    else:
      # Mettre à jour les coefficients de Bezout en fonction des résultats obtenus
      pgcd, x, y = euclideEtendu(b % a, a)
      # Retourner le PGCD, coeffA, et coeffB

      print(repr((pgcd, y - (b // a) * x, x)))
      return pgcd, y - (b // a) * x, x

def inverseModulaire (e, m) : 
   r, u, v = euclideEtendu(e, m)
   if r == 1 : 
      return u % m

"""
    demanderNombre
    -> Demande à l'utilisateur un nombre
"""
def demanderNombre(val):
    while True:
        try:
            x = int(input("Entrez " + val + ": "))
            return x;
        except ValueError:
            print("/!\ Cette valeur n'est pas un chiffre valide.")

"""
    demanderNombrePremier(val)
    -> Demande à l'utilisateur un nombre premier
"""
def demanderNombrePremier(val):
    while True:
        try:
            x = int(input("Entrez " + val + ": "))

            if estNombrePremier(x) == False:
                raise Exception()

            return x;
        except ValueError:
            print("/!\ Cette valeur n'est pas un chiffre valide.")
        except Exception:
            print("/!\ Cette valeur n'est pas un nombre premier.")

def genererCles():
  p = 0
  q = 0
  e = 0

  while not (estNombrePremier(p) and p != q):
    print("P: " + repr(p) + ", Q: " + repr(q));
    p = random.randint(0, 100)

  while not (estNombrePremier(q) and p != q):
    print("P: " + repr(p) + ", Q: " + repr(q));
    q = random.randint(0, 100)
  
  n = p * q
  indicEuler = (p - 1) * (q - 1)

  print("P = " + repr(p) + " | Q = " + repr(q));
  print("L'indicatrice Euler (p - 1) * (q - 1) = " + repr(indicEuler));


  while True:
      try:
          e = int(input("Choisir un entier naturel inférieur à l'indice Euler pour l'exposant de chiffrement:"))

          if e > indicEuler:
            raise ValueError()

          if premiersentreeux(e, indicEuler) == False:
            raise Exception()
          break;

      except ValueError:
          print("/!\ Cette valeur n'est pas un chiffre inférieur à l'indice Euler.")
      except Exception:
          print("/!\ Cette valeur n'est pas un nombre premier inférieur à l'indice Euler.")
  
  d = inverseModulaire(e, indicEuler)
  return (e, n), (d, n)

"""
  chiffrerTexte(texte)
  -> Chiffre un texte à l'aide d'un couple de clés publiques et génère un couple de clés privées pour pouvoir le déchiffrer
"""
def chiffrerTexte(texte):
  print("--- [ Chiffrement de texte ] ---")

  texte = texte or "Hello World!"
  (e, n), (d, n) = genererCles()
  
  print("Texte à chiffrer: " + texte)
  print("Clé publique: " + repr((e, n)))
  print("Clé privée: " + repr((d, n)))

  # On prend chaque caractère du tableau, on récupère sa valeur
  # ASCII, et on refait une boucle pour reconvertir en chaîne de caractères
  tableau = []
  for char in texte:
    tableau.append(
      ord(char) ^ e % n
    )

  texteChiffre = ''
  for ascii in tableau:
    texteChiffre += chr(ascii)
  
  print("Texte chiffré: \"" + texteChiffre + '"')

  choix = input("Déchiffrer ce même message? (O/N)")
  print("Choix: " + choix)
  if (choix in ("o", "O", "oui", "Oui")):
    print("Pour déchiffrer ce texte, vous aurez besoin du couple suivant: " + repr((d, n)))
    dechiffrerTexte(texteChiffre)
  else: input("Appuyez sur Entrée pour continuer...")

def dechiffrerTexte(texte):
  print("--- [ Déchiffrement de texte ] ---")
  print("Texte à déchiffrer: " + texte)

  d = demanderNombre("d")
  n = demanderNombre("n")

  print("Clé privée: " + repr((d, n)))

  tableau = []
  for char in texte:
    tableau.append(
      ord(char) ^ d % n
    )

  texteDechiffre = ''
  for ascii in tableau:
    texteDechiffre += chr(ascii)
  
  print("Texte déchiffré: \"" + texteDechiffre + '"')
  input("Appuyez sur Entrée pour continuer...")