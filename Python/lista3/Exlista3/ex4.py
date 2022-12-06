lista = []
vogal = ["a","A","e","E","i","I","O","o","u","U"]
contador = 0
vogais = 0
total = len(lista)
while contador < 510:
    letra = input("insira uma letra:")
    contador += 1
   lista.append(letra)
for x in lista:
  if x in vogal:
    vogais += 1
  else:
    print(x)
consoantes = total - vogais
print(consoantes)