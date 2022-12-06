loop = 0
numin = 0
numout = 0

while loop<10:
    num = int(input('Insira um número: '))
    if num<10 or num>20:
        numout += 1
    else:
        numin += 1
    loop +=1
print(f"{numout} Estão fora e {numin} estão dentro do intervalo [10,20]")