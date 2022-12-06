comparadordedano = nascimento.pop(2)

if comparadordedano >= 2000:
    flag = 0
    nascimento.append(comparadordedano)
elif comparadordedano < 2000:
    flag = 1
    nascimento.append(comparadordedano)

for x in nascimento:
    if nascimento.index(x) == 1:
        if x in mes1:
            z = (nascimento.pop(1))*28
            nascimento.insert(1, z)
        elif x in mes2:
            z = (nascimento.pop(1))*30
            nascimento.insert(1, z)
        elif x in mes3:
            z = (nascimento.pop(1))*31
            nascimento.insert(1, z)
    elif nascimento.index(x) == 2:
        nascimento.pop(2)
        calibracao = calibracaobisexto - x
        if calibracao < 0:
            calibracao = calibracao + 4
        while contadorloop < calibracao:
            contadorloop += 1
            if contadorloop %4 == 0:
                contadorcalibracao += 1
        z = (x*365)+contadorcalibracao
        nascimento.insert(2, z)

for x in dataatual:
    if dataatual.index(x) == 1:
        if x in mes1:
            z = (dataatual.pop(1))*28
            dataatual.insert(1, z)
        elif x in mes2:
            z = (dataatual.pop(1))*30
            dataatual.insert(1, z)
        elif x in mes3:
            z = (dataatual.pop(1))*31
            dataatual.insert(1, z)
    elif dataatual.index(x) == 2:
        dataatual.pop(2)
        calibracao = calibracaobisexto - x
        if calibracao < 0:
            calibracao = calibracao + 4
        while contadorloop < calibracao:
            contadorloop += 1
            if contadorloop %4 == 0:
                contadorcalibracao += 1
        z = (x*365)+contadorcalibracao
        dataatual.insert(2, z)



dia = dataatual.pop(0)-nascimento.pop(0)
mes = dataatual.pop(0)-nascimento.pop(0)
ano = dataatual.pop(0)-nascimento.pop(0)

total = dia+mes+ano

while total >= 0:
    total = total - 7
if total < 0:
    total = total + 7

if flag == 0:
    processandoodia = intdiadasemana + total
elif flag == 1:
    processandoodia = intdiadasemana + total-1

print(processandoodia)
for x in diadasemana:
    if diadasemana.index(x) == processandoodia:
        diadonascimento += x
        
print(diadonascimento)