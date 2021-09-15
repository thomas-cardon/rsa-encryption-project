import os

print("Programme de chiffrement")
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
print("P: " + repr(p) + " | Q: " + repr(q));
