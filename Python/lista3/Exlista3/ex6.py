media = []
contador = 0
loop = 0
nota = 1
singlemedia = 0
totmed = 0
aprovados = 0
while contador < 10:
  notas = float(input(f"Insira a {nota}° nota: "))
  singlemedia += notas
  loop += 1
  nota += 1
  if loop == 4:
    contador += 1
    loop = 0
    nota = 1
    totmed = singlemedia/4
    media.append(totmed)
for x in media:
  if x >= 7:
    aprovados += 1
print(aprovados)