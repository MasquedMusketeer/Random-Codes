base = int(input('Insira a base: '))
expo = int(input('Insira o exponente: '))
loop = 1
resultado = base

while loop < expo:
    resultado *= base
    loop += 1
print(f'{base}^{expo} = {resultado}')