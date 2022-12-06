def teste(x):
    contador = x
    flag = 0
    while contador > 0:
        if x % contador == 0:
            flag += 1
        contador -= 1
    if flag == 2:
        res = 1
    else:
        res = 0
    return res

Numero = int(input('Insira um numero inteiro: '))
contador_script = Numero
flag_total = 0
while contador_script > 0:
    if teste(contador_script) == 1:
        flag_total += 1
    contador_script -= 1
print(f'Existem {flag_total} Primos entre {Numero} e zero.')