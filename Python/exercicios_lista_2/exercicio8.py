sequencia = int(input('Insira a quantidade de sequencias desejada: '))
loop = 0
start = 1
next = start
print(start)
while loop < sequencia:
    print(next)
    dummy = start + next
    start = next
    next = dummy
    loop += 1
