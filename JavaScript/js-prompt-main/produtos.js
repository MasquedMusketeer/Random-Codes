const input = require('prompt-sync')()

    console.log ("Lista De Compras do seu zé")

    let p1 = parseFloat(input('Preço do primeiro produto: R$'))
    let p2 = parseFloat(input('Preço do segundo produto: R$'))
    let p3 = parseFloat(input('Preço do terceiro produto: R$'))
    let p4 = parseFloat(input('Preço do quarto produto: R$'))
    let p5 = parseFloat(input('Preço do quinto produto: R$'))
    let p6 = parseFloat(input('Preço do sexto produto: R$'))
    
    let t = p1 + p2 + p3 + p4 + p5 + p6
    t = parseFloat(t)
    
    console.log (`Seu total é de R$${t}`)
    console.log (`débito ou crédito ?`)

  do {
       var fop = parseFloat(input('Para débito pressione 0 e para crédito pressione 1: '))

       
       if(fop == 0){
        console.log('Você selecionou Débito')}
        else if(fop == 1){
        console.log('Você selecionou Crédito')}
        else {
            console.log('Selecione um numero válido')
        }
    }
    while (fop>1)

       

    
    console.log('Obrigado e volte sempre!!!')

