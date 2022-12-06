loop = 0

while loop == 0:
    tabuada = int(input('Insira um número(1-10): '))
    if tabuada<0 or tabuada>10:
        print('Insira um número válido.')
    else:
        loop = 1

contador = 0
valormult = 1

while contador <10:
    total = valormult*tabuada
    print(f"{tabuada} x {valormult} = {total}")
    contador += 1
    valormult += 1

