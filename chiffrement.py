import os, sys

print("Programme de chiffrement")
#Choisir deux nombres premiers
text = input("Entrez le texte: ")

p = None
q = None
e = None

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

while True:
    try:
        p = int(input("Entrez p: "))

        if estNombrePremier(p) == False:
            raise Exception()


        break;
    except ValueError:
        print("/!\ Cette valeur n'est pas un chiffre valide.")
    except Exception:
        print("/!\ Cette valeur n'est pas un nombre premier.")

while True:
    try:
        q = int(input("Entrez q: "))

        if estNombrePremier(q) == False:
            raise Exception()

        break;
    except ValueError:
        print("/!\ Cette valeur n'est pas un chiffre valide.")
    except Exception:
        print("/!\ Cette valeur n'est pas un nombre premier.")

os.system('cls||clear')

print("Texte reçu: " + text)
print("P: " + repr(p) + " | Q: " + repr(q))
#module chiffrement :
n = p * q
print("Module de chiffrement (n) = " + repr(n))

indicEuler = (p - 1) * (q - 1)
print("Indicatrice Euler = " + repr(indicEuler))

def pgcd(a,b):
    while b:
        a, b = b, a%b
    return a
    
def premiersentreeux(a,b):
    if(pgcd(a,b) == 1 ):
        return True
    return False



while True:
    try:
        e = int(input("Choisir un entier naturel inférieur à l'indice Euler pour l'exposant de chiffrement:"))
        
        if e > indicEuler:
            raise ValueError()
        
        if premiersentreeux(e,indicEuler) == False:
           raise Exception()
        break;
    
    except ValueError :
        print("/!\ Cette valeur n'est pas un chiffre inférieur à l'indice Euler.")
    except Exception:
        print("/!\ Cette valeur n'est pas un nombre premier à l'indice Euler.")

print("{0}: {1}".format("P", p))
print("{0}: {1}".format("Q", q))
print("{0}: {1}".format("E", e))

def euclideEtendu(a, b):
    # L'algorithme s'arrête quand on trouve 0 
    if a == 0:
        return b, 0, 1
    else:
      # Mettre à jour les coefficients de Bezout en fonction des résultats obtenus 
      pgcd, x, y = euclideEtendu(b % a, a)
      # Retourner le PGCD, coeffA, et coeffB
      return pgcd, y - (b // a) * x, x

d = euclideEtendu(e, indicEuler)[1] # Obtenir le coeff. a, soit la clé de déchiffrement

print("{0}: {1}".format("D", d))

