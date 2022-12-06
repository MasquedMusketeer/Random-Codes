const input = require('prompt-sync')()

var code = parseInt(input('Código do produlto: '))
var quantidade = Number(input('Quantidade do produto a ser comprado: '))

if (code === 1){
    var valor = 5.00
}else if (code === 2){
    var valor = 3.50
}else if (code === 3){
    var valor = 4.80
}else if (code === 4){
    var valor = 8.90
}else if (code === 5){
    var valor = 7.32
}

var payment = quantidade*valor

console.log(`Valor a ser pago: R$${payment.toFixed(2)}`)