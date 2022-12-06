loop = 0
idadet = 0

while loop <50:
    idade = int(input('Insira uma idade: '))
    idadet += idade
    loop += 1

media = idadet/50
print(f'A média entre elas é {media} anos')