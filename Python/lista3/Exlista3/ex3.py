listanotas = [ ]
contador = 0
media = 0
while contador < 54:
    notas = float(input("Insira um numero: "))
    contador += 1
   listanotas.append(notas)
for x in listanotas:
    media += x
print(listanotas)
print(media)