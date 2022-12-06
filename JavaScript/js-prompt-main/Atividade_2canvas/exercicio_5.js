const input = require('prompt-sync')()

var n1 = parseInt(input('Insira um número: '))
var n2 = parseInt(input('Insira um número: '))
var n3 = parseInt(input('Insira um número: '))

var s1 = n1-n2
var s2 = n2-n3
var s3 = n1-n3
var s4 = s1+s2+s3

if(s4>0 || s4<0){
if(s1<=0 && s3<0){
    console.log(`menor ${n1}`)
}
else if(s1>=0 && s2<0){
    console.log(`menor ${n2}`)
}
else if(s2>=0 && s3>0){
    console.log(`menor ${n3}`)
}}
else{
    console.log('São iguais.')
}