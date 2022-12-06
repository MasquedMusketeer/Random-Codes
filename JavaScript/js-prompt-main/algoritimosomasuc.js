const input = require('prompt-sync')()


var N1 = Number(input(`Insira o primeiro numero: `))

var N2 = Number(input(`Imsira o segundo numero: `))

var Nr = N1

var Nop = 1

do {
    var Nr = Nr + N1
    
    var Nop = Nop + 1
    
}
while(Nop<N2)


console.log(`O resultado da multiplicação é ${Nr}`)