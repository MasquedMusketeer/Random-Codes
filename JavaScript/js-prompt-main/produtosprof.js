const input = require('prompt-sync')()

    console.log ("Lista De Compras do seu zé")

    receberProduto = true
    let produtos = []

    do {
        let produto = Number(input('Digite o preço do produto: R$ '))

        produtos.push(produto)

        console.log('Deseja adicionar mais alguma coisa?')
        let resposta = input('Digite 0 para não e 1 para sim: ')

        if (resposta === '0') {
            receberProduto = false}
            else if (resposta === 1){
                receberProduto = true}
                else {
                    console.log('Selecione um numero válido')
                }
            
    } while (receberProduto)

    let total = 0

    produtos.map(produto => {
        total = total + produto
        return
    })

    console.log(`O total das compras é R$ ${total}`)
    console.log ('débito ou crédito ?')
    
    do {
    var fop = Number(input('Para débito pressione 0 e para crédito pressione 1: '))


    
    if(fop === 0){
     console.log('Você selecionou Débito')}
     else if(fop === 1){
     console.log('Você selecionou Crédito')}
     else {
         console.log('Selecione um numero válido')
     }
 }
 while (fop>1)
 
       

    
    console.log('Obrigado e volte sempre!!!')

