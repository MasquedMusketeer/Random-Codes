def celcius_farenheint(x):
    temp = (x*1.8)+32
    return temp
def farenheint_celcius(y):
    temp = (y-32)/1.8
    return temp
def menu(z):
    if  z == 1:
        print(celcius_farenheint(float(input('Insira a temperatura: '))))
    elif z == 2:
        print(farenheint_celcius(float(input('Insira a temperatura: '))))
print(menu(int(input('1-Converte Celcius para Farenheint  2-Converte Farenheint para Celcius: '))))