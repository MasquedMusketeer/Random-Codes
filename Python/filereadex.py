file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\file1.txt', mode = 'a', encoding = 'utf-8')
def quebra_de_item():
    file.write('*****************************')
def quebra_de_linha():
    file.write('\n')
counterprogram = 0
def texto_1():
    file.write('Números pares de 0 à 20')
def texto_2():
    file.write('Rumo ao Hexa')
def contador():
    contador = 0
    while contador < 21:
        if contador % 2 == 0:
            file.write(str(contador))
            quebra_de_linha()
        contador += 1

while counterprogram < 7:
    if counterprogram == 0 or counterprogram == 2 or counterprogram == 4 or counterprogram == 6:
        quebra_de_item()
        quebra_de_linha()
    elif counterprogram == 1:
        texto_1()
        quebra_de_linha()
    elif counterprogram == 3:
        contador()
    elif counterprogram == 5:
        texto_2()
        quebra_de_linha()
    counterprogram += 1

file.close()