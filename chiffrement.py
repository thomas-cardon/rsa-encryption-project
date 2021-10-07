import os


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
    while b:
        a, b = b, a%b
    return a

"""
    premiersentreeux(a,b)
    -> Vérifie si a et b sont premiers entre eux
"""
def premiersentreeux(a,b):
    if(pgcd(a,b) == 1 ):
        return True
    return False

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
      return pgcd, y - (b // a) * x, x


def start():
    os.system('cls||clear')

    print("Programme de chiffrement")
    text = input("Entrez le texte à chiffrer: ")
    p = q = n = indicEuler = e = d = None

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

    n = p * q
    indicEuler = (p - 1) * (q - 1)

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

    d = euclideEtendu(e, indicEuler)[1]

    print("{0}: {1}".format("Texte", text))
    print("{0}: {1}".format("P", p))
    print("{0}: {1}".format("Q", q))
    print("{0}: {1}".format("E", e))
    print("{0}: {1}".format("N", n))
    print("{0}: {1}".format("E", e))
    print("{0}: {1}".format("D", d))

start()