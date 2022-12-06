const input = require('prompt-sync')()

var Db = parseFloat(input('insira o dia de nascimento: '))

var Mb = parseFloat(input('insira o mes de nascimento: '))

var Yb = parseFloat(input('insira o ano de nascimento: '))

var Dp = parseFloat(input('insira o dia de hoje: '))

var Mp = parseFloat(input('insira o mes atual: '))

var Yp = parseFloat(input('insira o ano atual: '))

var Di = Dp-Db

var Mi = Mp-Mb

var Yi = Yp-Yb

if(Di<0){
    Dr = Di+30
    Mr = Mi -1
}else{
    Dr = Di
    Mr = Mi
}

if(Mr<0){
    Mrf = Mr+12
    Yr = Yi-1
}else{
    Mrf = Mr
    Yr = Yi
}


var Md = Mrf*30

var Yd = Yr*365

var Iid = Dr+Md+Yd

console.log(`sua idade em dias é :${Iid}`)
