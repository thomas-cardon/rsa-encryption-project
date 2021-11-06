from chiffrement import chiffrer, choixCle, clePublique

def start():
  p, q, e = choixCle(100, 1000)
  pub = clePublique(p, q, e)

  print("P: {0} | Q: {1} | E: {2}".format(p, q, e))
  print("Clé publique: " + repr(pub))

  bytearr = []

  with open("audio.wav", "rb") as f:
    fc = f.read()
    while(fc):
      bytearr.append(chiffrer(int.from_bytes(fc, "big"), pub))

  with open("encrypted.wav", "w") as f:
    f.write(bytes(bytearr))

start()