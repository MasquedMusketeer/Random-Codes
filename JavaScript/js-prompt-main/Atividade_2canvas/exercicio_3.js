const input = require('prompt-sync')()

var valor = Number(input('Valor do produto a ser comprado: '))
var quantidade = Number(input('Quantidade do produto a ser comprado: '))
var pagamento = Number(input('Valor do pagamento dado pelo cliente: '))

var preco = valor*quantidade
var troco = pagamento-preco

if(troco>=0){
    console.log(`O troco a ser dado é de R$${troco.toFixed(2)}`)
}
else{
    var troco = troco*-1
    console.log(`O valor não foi o suficiente, o cliente ainda deve dar R$${troco.toFixed(2)}`)
}