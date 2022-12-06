loop1 = 0
odd = 0
even = 0

while loop1<10:
    number = int(input('Insira um número: '))
    verify = number
    while verify>0:
        verify -= 2
    if verify == 0:
        even += 1
    else:
        odd += 1
    loop1 += 1

print(f'{even} são pares e {odd} são impares')
