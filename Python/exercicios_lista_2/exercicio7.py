n1 = float(input('Insira um número: '))
loop = 0
comp = n1
while loop < 4:
    n = float(input('Insira um número: '))
    if n > comp:
        comp = n
    loop += 1
print(f'{comp} é o menor')