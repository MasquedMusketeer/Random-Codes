const input = require('fs').readFileSync('stdin','utf-8')
let valores = input.split('\n\r')
let nota1 = Number(valores[0])
let nota2 = Number(valores[1])
let nota3 = Number(valores[2])
let nota4 = Number(valores[3])
let media = (nota1+nota2+nota3+nota4)/4
console.log(`media = ${media.toFixed(1)}`)