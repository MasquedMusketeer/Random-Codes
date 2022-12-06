def soma_imposto(x, y):
    taxaimposto = x
    custo = y
    custo_imposto = (taxaimposto/100) * custo
    custo_total = custo + custo_imposto
    return round(custo_total,2)
print(soma_imposto(float(input('Insira a taxa de imposto sobre as vendas em porcentagem: ')),float(input('Insira o custo do produto antes do imposto: '))))