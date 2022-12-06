aluno = [{
    'nome' : 'Armando João',
    'notas' : [5,7,3,8],
    'media' : '',
    'condicao' : ''
},{
   'nome' : 'Rodrigo Santana',
    'notas' : [2,4,5,8],
    'media' : '',
    'condicao' : '' 
}]
MediaCalculo = 0
for x in aluno:
    for y in x.keys():
        if y == 'media':
            for z in x['notas']:
                MediaCalculo += z
            x[y] = MediaCalculo/4
            MediaCalculo = 0
        if y == 'condicao':
            if x['media'] >= 6:
                x[y] = 'Aprovado'
            else:
                x[y] = 'Reprovado'
print(aluno)