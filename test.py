def euclideEtendu(a, b): 
    # L'algorithme s'arrête quand on trouve 0 
    if a == 0 :  
        return b,0,1
             
    pgcd, temp_coeffA, temp_coeffB = euclideEtendu(b % a, a) 
     
    # Mettre à jour coeffA et coeffB en fonction des résultats obtenus 
    coeffA = temp_coeffA - (b // a) * temp_coeffA 
    coeffB = temp_coeffB 
     
    return pgcd, coeffA, coeffB

def euclideEtendu(a, b):
    # L'algorithme s'arrête quand on trouve 0 
    if a == 0:
        return b, 0, 1
    else:
      # Mettre à jour les coefficients de Bezout en fonction des résultats obtenus 
      pgcd, x, y = euclideEtendu(b % a, a)
      # Retourner le PGCD, coeffA, et coeffB
      return pgcd, y - (b // a) * x, x

print(euclideEtendu(43, 4))