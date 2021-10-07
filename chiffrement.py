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
        e = int(input("choisir un entier naturel inférieur à l'indice Euler:"))
        
        if e > indicEuler:
            raise ValueError()
        
        if premiersentreeux(e,indicEuler) == False:
           raise Exception()
        break;
    
    except ValueError :
        print("/!\ Cette valeur n'est pas un chiffre inférieur à l'indice Euler.")
    except Exception:
        print("/!\ Cette valeur n'est pas un nombre premier à l'indice Euler.")

def exposantdechiffrement(a,b):

    if pgcd(a,b) == 1:
        c = None
        d = None
        e = None
        f = None
        g = None

        a = c * d + e
        b = e * f + g
        
    if g == 1:
        g = b*1 - e*f
        g =  

    elif e == 1:
        e = a*1 - c*d

    else :
      print("/!\ ça ne marche point.")


    
          


        
    # x = a*u + b*v;  u = indice de chiffrement
    # if x == 1:
    #        return u
    #    else:
    #        return -1
    #else:
    #    raise Exception() ```

#print("l'exposant de chiffrement est:");
#print ("u")
#print(lexposantdechiffrement(e, indicEuler));


