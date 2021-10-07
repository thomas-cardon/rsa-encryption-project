import os

print("Programme de chiffrement")
#Choisir deux nombres premiers
text = input("Entrez le texte: ")

p = None
q = None

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
#moul e chiffrement :
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
        e = int(input("choisir un entier naturel inférieur à l'indice Euler:"))
        
        if e > indicEuler:
            raise ValueError()
        
        if premiersentreeux(e,indicEuler) == True:
           raise Exception()
        break;
    
    except ValueError :
        print("/!\ Cette valeur n'est pas un chiffre inférieur à l'indice Euler.")
    except Exception:
        print("/!\ Cette valeur n'est pas un nombre premier à l'indice Euler.")
