def definicao_de_sinal(x):
    if x == 0:
        res = 'Neutro'
    elif x > 0:
        res = "Positivo"
    elif x < 0:
        res = "Negativo"
    return res

print(definicao_de_sinal(float(input('Insira  um número: '))))