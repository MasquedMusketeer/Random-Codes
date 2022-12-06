lista = []
contador = 0
while contador < 10:
  value = float(input("Insira o valor: "))
  lista.append(value)
  contador += 1
print(lista)
list(reversed(lista))
print(lista)