flag = 0
lista1 = []
lista2 = []
lista3 = []
contador = 0
while contador < 20:
  if flag == 0:
    value = input("insira um caractere: ")
    lista1.append(value)
    contador += 1
    if contador == 9:
      flag += 1
  elif flag == 1:
    value = input("insira um caractere: ")
    lista2.append(value)
    contador += 1
flag -= 1
contador = 0
while contador < 20:
  if flag == 0:
    value = lista1.pop(0)
    lista3.append(value)
    lista1.append(value)
    flag += 1
  elif flag == 1:
    value = lista2.pop(0)
    lista3.append(value)
    lista2.append(value)
    flag -= 1
  contador += 1
print(lista1)
print(lista2)
print(lista3)