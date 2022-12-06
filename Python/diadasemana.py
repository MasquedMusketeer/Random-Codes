nascimento = []
dataatual = []
processing = []
mes1 = [2]
mes2 = [1,3,5,7,8,10,12]
mes3 = [4,6,9,11]
diadasemana = ["segunda", "terça", "quarta","quinta", "sexta", "sábado","domingo"]
calibracaobisexto = 2020  #Deve ser inserido o último ano bisexto ocorrido
contadorcalibracao = 0
contadorloop = 0
diadonascimento = 'Você nasceu na '
diaprevisto = "Hoje"

usrinputnasc = input('Insira sua data de nascimento(use espaço para separar os números): ')
usrinputatual = input('Insira a data de hoje(use espaço para separar os números): ')
usrinputdiadasemana = input("hoje é segunda, terça, quarta, quinta, sexta, sábado ou domingo? ")
intdiadasemana = diadasemana.index(usrinputdiadasemana)

nasc = usrinputnasc.split()
for x in nasc:
    nascimento.append(int(x))
hoje = usrinputatual.split()
for x in hoje:
    dataatual.append(int(x))

dia = nascimento.pop(0)
nascimento.insert(0, dia)
processing.append(dia)
mes = nascimento.pop(1)
nascimento.insert(1, mes)
processing.append(mes)
ano = dataatual.pop(2)
dataatual.insert(2, ano)
processing.append(ano)

mesfin = dataatual.pop(1)
dataatual.insert(1, mesfin)
mesini = processing.pop(1)
processing.insert(1, mesini)

diafin = dataatual.pop(0)
dataatual.insert(0, diafin)
diaini = processing.pop(0)
processing.insert(0, diaini)

diferencadedias = 0

while mesini < mesfin:
    if mesini in mes1 and ano % 4 == 0:
        diferencadedias += 29
    elif mesini in mes1 and ano % 4 != 0:
        diferencadedias += 28
    elif mesini in mes2:
        diferencadedias += 31
    elif mesini in mes3:
        diferencadedias += 30
    mesini += 1

diastotais = diferencadedias + (diafin-diaini)

while diastotais > 0:
    diastotais -= 7
if diastotais < 0:
    diastotais += 7

diaprocessing = intdiadasemana - diastotais

for x in diadasemana:
    if diadasemana.index(x) == diaprocessing:
        diaprevisto = x
posicaoatual = diadasemana.index(diaprevisto)

anoini = nascimento.pop(2)
nascimento.append(anoini)
anodecomeco = calibracaobisexto - anoini
contadordeposicoes = 0

while anodecomeco > 0:
    anodecomeco -= 4
    contadordeposicoes += 5
if anodecomeco < 0:
    anodecomeco += 4
    contadordeposicoes += (anodecomeco + 1)

while contadordeposicoes > 0:
    contadordeposicoes -= 7
if contadordeposicoes < 0:
    contadordeposicoes += 7

posicaocalculada = (posicaoatual - (contadordeposicoes + (ano - calibracaobisexto))) + 7
print(posicaoatual)
print(contadordeposicoes)
print(posicaocalculada)
for x in diadasemana:
    if diadasemana.index(x) == posicaocalculada:
        diacalculado = x
diaprevisto = diacalculado

print('Você nasceu', diaprevisto)