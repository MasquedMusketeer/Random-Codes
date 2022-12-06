idade = []
altura = []
contador = 0
while contador < 5:
  age = int(input("Sua idade: "))
  height = float(input("Sua altura"))
  idade.append(age)
  altura.append(height)
  contador += 1
idade = reversed(idade)
altura = reversed(altura)
print(idade)
print(altura)