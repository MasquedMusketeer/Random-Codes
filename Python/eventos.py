di = int(input('Dia de inicio do evento: '))
moni = int(input('Mês de inicio do evento: '))
hi = int(input('Hora de inicio do evento: '))
mini = int(input('Minutos de inicio do evento: '))
seci = int(input('Segundos de inicio do evento: '))


df = int(input('Dia de finalização do evento: '))
monf = int(input('Mês de finalização do evento: '))
hf = int(input('Hora de finalização do evento: '))
minf = int(input('Minutos de finalização do evento: '))
secf = int(input('Segundos de finalização do evento: '))

deltad = df-di
deltamon = monf-moni

if deltad < 0:
     deltad = deltad+30
     deltamon = deltamon-1


list1 = [1,3,5,7,8,10,12]
list2 = [2]
list3 = [4,6,9,11]

if moni in list2:
    monsize = 28

if moni in list3:
    monsize = 30

if moni in list1:
    monsize = 31

mont = deltamon*monsize
dt = deltad+mont

#horas

ht = hf-hi

if ht<0:
    ht = ht+24
    dt = dt-1

else:
    ht = ht
    dt = dt


# minutos

mint = minf-mini

if mint<0:
    mint = mint+60
    ht = ht-1


#seguntos

sect = secf-seci

if sect<0:
   sect = sect+60
   mint = mint-1


#promtp

print(f'O evento durou {dt} dias, {ht} horas, {mint} minutos e {sect} segundos.')