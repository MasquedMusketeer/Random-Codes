conducaotot = 0
loopend = 0
loopcount = 0
trajectory = 1
contador = 0
estado = 'Ida'
trajstate = 0
while loopend<1:
  imput = float(input(f'{estado},Aguardando valor: '))
  if imput == 1:
    contador = 1
    trajstate = 1
  elif imput == 0:
    contador = 0
    trajstate = 1
  elif imput == 10:
    loopend = 1
    trajstate = 0
  else:
    conducaotot += imput
    loopcount += 1
    trajstate = 0
  if contador == 0:
    estado = 'Ida'
  else:
    estado = 'Volta'
  if contador == 0 and trajstate == 1 or contador == 1 and trajstate == 1:
    trajectory += 1
conducaotot = round(conducaotot, 2)
print(f'Foram feitas {trajectory} viagens, {loopcount} passageiros usaram o transporte e foi arrecadado R${conducaotot}')