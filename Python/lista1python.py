#Exercicio 1:

n1 = int(input('Insira um número: '))
if n1 == 0 :
    print('o valor é zero.')
elif n1 > 0:
    print('O valor é positivo.')
else:
    print('o valor é negativo')

#Exercicio 2:

num1 = int(input('Insira um número: '))
num2 = int(input('Insira um número: '))
num3 = int(input('Insira um número: '))

if num1 > num2 and num2 > num3:
    print('O primeiro é o maior e o terceiro é o menor')
elif num2 > num1 and num1 > num3:
    print('O segundo é o maior e o terceiro é o menor')
elif num3 > num2 and num2 > num1:
    print('O terceiro é o maior e o primeiro é o menor')
elif num2 > num3 and num3 > num1:
    print('O segundo é o maior e o primeiro é o menor')
elif num3 > num1 and num1 > num2:
    print('O terceiro é o maior e o segundo é o menor')
elif num1 > num3 and num3 > num2:
    print('O primeiro é o maior e o segundo é o menor')
else:
    print('Os número são iguais!!!')

#Exercicio 3:

turno = input('Em que turno você estuda?(M,V ou N): ')

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Insira um caractere valido.')

#Exercicio 4:

Dow = int(input('insira um numero entre 1 e 7: '))

if Dow > 0 and Dow < 8:
    if Dow == 1:
        print('Domingo')
    elif Dow == 2:
        print('Segunda-feira')
    elif Dow == 3:
        print('Terça-feira')
    elif Dow == 4:
        print('Quarta-feira')
    elif Dow == 5:
        print('Quinta-feira')
    elif Dow == 6:
        print('Sexta-feira')
    elif Dow == 7:
        print('Sábado')
else:
    print('Insira um caractere valido.')

#Exercicio 5:

number1 = int(input('Insira um numero: '))
number2 = int(input('Insura um numero: '))

if number1 > number2:
    print('o primeiro é o maior')
else:
    print('o segundo é o maior')

#Exercicio 6:

Number1 = int(input('Insira um numero: '))
Number2 = int(input('Insura um numero: '))

if Number1 > Number2:
    nt = Number1 - Number2
    print(f'o primeiro é o maior e a diferença entre eles é {nt}')
else:
    nt = Number2 - Number1
    print(f'o segundo é o maior e a diferença entre eles é {nt}')

#Exercicio 7:

Data1 = input('Insira seu sexo(m ou f): ')
Data2 = float(input('Insira sua altura(em metros): '))

if Data1 == 'm':
    pi = (72.7*Data2)-58
    print(f'Seu peso ideal é {pi}')
elif Data1 == 'f':
    pi = (62.1*Data2)-44.7
    print(f'Seu peso ideal é {pi}')