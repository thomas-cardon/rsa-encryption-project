from random import randint

def pgcd(a, b):
    print("Calcul PGCD(a =", a, "b =", b, ")")
    while a != b:
      if (a > b):
        a = a - b
      else:
        b = b - a

    print("Résultat: ", a)
    return a

def premierAleatoire(debut, ecart):
    n = randint(debut, debut + ecart)  # fin=debut+ecart
    while not estPremier(n):
        n = randint(debut, debut + ecart)
    return n

def premierAleatoireAvec(n):
    m = randint(2, n - 1)

    while pgcd(m, n) != 1:
        m = randint(2, n - 1)
        print(2, n - 1, m)
    return m

"""
    euclideEtendu(a,b)
    -> Calcule le PGCD ainsi qu'un des couples de coefficients de Bezout, c'est-à-dire deux entiers u et v tels que au + bv = PGCD(a, b)
"""
def euclideEtendu(a,b):
    r = a
    u = 1
    v = 0
    rp = b
    up = 0
    vp = 1
    #  rs, us, vs  variables de stockage intermédiaires
    
    while rp != 0:
      print("--- nouvelle étape");
      print("a ", a);
      print("b ", b);
      print("r ", a);
      print("u ", 1);
      print("v ", v);
      print("rp ", rp);
      print("up ", up);
      print("vp ", vp);

      q = r // rp # division entière
      rs = r
      us = u
      vs = v
      r = rp
      u = up
      v = vp
      rp = rs - q * rp
      up = us - q * up
      vp = vs - q * vp
    
    print("euclide etendu")
    return r, u, v


def estPremier(num):
    num = int(num)
    if num < 2: return False
    else:
        if num > 2 and num % 2 == 0:
            return False
        for x in range(2, num // 2):
            if num % x == 0:
                return False
        return True


def inverseModulaire(e, m):  # A comprendre ou à refaire
    r, u, v = euclideEtendu(e, m)
    if r == 1:
        return u % m


def exponentiationModulaire(M, e, n) :
  return pow(M, e) % n # C = M^e mod n


def choixCle(min, max):
    p = premierAleatoire(min, max)
    q = premierAleatoire(p + 1, max)
    e = premierAleatoireAvec((p - 1) * (q - 1))
    # phi(n), l'indicatrice d'Euler en n
    return p, q, e


def clePublique(p, q, e):
    return p * q, e


def clePrivee(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverseModulaire(e, phi)
    return n, d


"""
    demanderNombre
    -> Demande à l'utilisateur un nombre
"""


def demanderNombre(val):
    while True:
        try:
            x = int(input("Entrez " + val + ": "))
            return x
        except ValueError:
            print("/!\ Cette valeur n'est pas un chiffre valide.")


def chiffrer(M, clePub):
    n, e = clePub
    if M < n:
        return exponentiationModulaire(M, e, n)


def dechiffrer(M, clePriv):
    n, d = clePriv
    if M < n:
        return exponentiationModulaire(M, d, n)
