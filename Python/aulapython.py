contador = 0
lista = []
while contador < 10:
    nome = input('Insira um nome: ')
    lista.append(nome)
    contador += 1
listamenor = []
for x in lista:
    palavra = lista.pop(0)
    tamanho = len(palavra)
    if tamanho < 5:
        listamenor.append(palavra)  
    else:
        lista.append(palavra) 
print(lista)
print(listamenor)