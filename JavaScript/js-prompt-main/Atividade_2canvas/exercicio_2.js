const input = require('prompt-sync')()

var minutos = Number(input('Quantidade de minutos usados: '))

if(minutos>100){
    var cobranca = minutos-100
    var valor = 50 + cobranca*2
}
else{
    var valor = 50
}
console.log(`O total a ser cobrado é de R$${valor.toFixed(2)}`)