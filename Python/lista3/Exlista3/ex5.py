todos = []
par = []
impar = []
contador = 0
while contador < 20:
  value = int(input("Insira um numero: "))
    contador += 1
   todos.append(value)
for x in todos:
  if x % 2 == 0:
    par.append(x)
  else:
    impar.append(x)
print(par)
print(impar)
print(todos)