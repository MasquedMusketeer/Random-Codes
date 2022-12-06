lista = []
contador = 0
mult = 1
soma = 0
while contador < 5:
  value = int(input("insira um numero: "))
  lista.append(value)
  contador += 1
for x in lista:
  mult *= x
  soma += x
print(lista)
print(mult)
print(soma)