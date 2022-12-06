meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
def data_por_extenso(x):
    data_lista = x.split('/')
    calculo_mes = int(data_lista.pop(1))
    for z in  meses:
        if (calculo_mes-1) == meses.index(z):
            mes_resultado = z
    dia = data_lista.pop(0)
    ano = data_lista.pop(0)
    data_resultado =dia + " de " + mes_resultado + " de " + ano
    if int(dia) > 31 or calculo_mes > 12 or  int(dia) < 1 or calculo_mes < 1 or int(ano < 0):
        return "NULL"
    else:
        return data_resultado
print(data_por_extenso(input('Insira uma data separada por "/" : ')))