frutas = ['manga','kiwi','morango','goiaba','ananas','tangerina','laranja']
vogal = ['A','a','E','e','I','i','O','o','U','u']
Frutas = []
flag = 0
for x in frutas:
    for i in x:
        if i in vogal:
            flag += 1
    if flag == 2 :
        Frutas.append(x)
    flag = 0
print(Frutas)