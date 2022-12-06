lista = []
contador = 0
soma = 0
quadrado = 0
while contador < 10:
  value = int(input("Insira o valor: "))
  lista.append(value)
  contador += 1
for x in lista:
  quadrado = x*x
  soma += quadrado
print(soma)