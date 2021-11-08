"""
    Voici la fonction Euclide Etendu avec le stockage dans des tableaux correspondant à a, au quotient et au reste, elle affiche seulement les équations utilisées pour l'algorithme d'Euclide étendu. Le resutat qui s'affiche est faux """

tableauA = []
tableauR = []
tableauQ = []


def pgcd(a, b):
    print("--- Calcul PGCD1 ---")
    while b:
        if b != 0:
            quotient = a // b

            print(a, "/", b)
            a, b = b, a % b
            """print("ancien b :", a," et reste de a/b :", b, "quotient :", quotient)"""
            print("ancien b :", a, "quotient :", quotient)
            tableauA.append(a)
            tableauR.append(b)
            tableauQ.append(quotient)
        else:
            print("ancien b :", a, " et reste de a/b :", b)
            tableauA.append(a)
    print("--- Fin Calcul PGCD ---")
    return a, b, quotient


print(pgcd(195, 154))
print("-----------------------")
print(tableauA, "A")
print(tableauR, "R")
print(tableauQ, "Q")
print("\n")


def euclideetendu(a, b):
    print("euclide")
    # on réécrit les équations en partant du bas et en isolant le reste
    print("------------------")

    a1 = a
    tableauY = []
    for i in range(len(tableauA) - 1):
      v = tableauQ[i]
      #r = tableauR[i]
      t = tableauA[i]
      z = v * t
      u = 1
      u1 = u
      v1 = v
      y = a1 * u - z
      o = a1, "", u1, "-", v1, "", t
      print(y, "=", a1, "", u, "-", v, "", t)
      tableauY.append(o)
      a1 = t

    print("------------------")

    """for i in reversed(range(len(tableauY))):
      a1 = tableauA[i]
      a2 = tableauA[i - 1]
      t = tableauY[i]
      v = tableauQ[i-1]
      print(y, "=", a1, "", u, "-", v, "", t)
      u = v1 + u
      v = u1 * v1
      print(y, "=", u, "", a1, "-", v, "", a2)"""

    print("------------------")

    #
    print()

    print("Resultats à trouver:"-15, 19)
    return u, v


print(euclideetendu(195, 154))