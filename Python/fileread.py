file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\file.txt', mode = 'r', encoding = 'utf-8')
calculocontador = []
for item in file:
    calculocontador.append(item)
counter = len(calculocontador)+1

file.close()

file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\file.txt', mode = 'a', encoding = 'utf-8')

traço = "-"
file.write(str(counter))
file.write(traço)
ursinpt = input('Insira um número: ')
file.write(ursinpt)
file.write('\n')

file.close()

file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\file.txt', mode = 'r', encoding = 'utf-8')

for item in file:
    print(item)
file.close()