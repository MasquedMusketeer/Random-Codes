var notat = 0
var contador = 0
var contadornota = 1
var contadorcalculo = 0
do{
    var nota = Number(input(`Insira a nota ${contadornota} do aluno: `))
    var notat = notat+nota
    var contador = contador+1
    var contadornota = contadornota+1
    var contadorcalculo = contadorcalculo+1
}
while(contador<4)
var media = notat/contadorcalculo
if(media<6){
    console.log(`Nota Média: ${media.toFixed(1)}, REPROVADO`)
}
else{
    console.log(`Nota Média: ${media.toFixed(1)}, APROVADO`)
}
