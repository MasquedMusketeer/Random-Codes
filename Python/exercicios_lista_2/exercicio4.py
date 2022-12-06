loop = 0
notat = 0

while loop <15:
    nota = int(input('Insira uma nota: '))
    notat += nota
    loop += 1

media = notat/15
print(f'A média entre elas é {media}.')