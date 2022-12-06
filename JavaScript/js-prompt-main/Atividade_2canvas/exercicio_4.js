const input = require('prompt-sync')()

var glicose = Number(input('Quantidade medida de glicose(em mg/dl): '))

if(glicose <=100){
    console.log('Seus níveis de glicose estão saudáveis.')
}
else if(glicose>100){
    if(glicose<=140){
        console.log('Seus níveis de glicose estão elevados, procure ajuda médica.')
    }
    else{
        console.log('Seus níveis de glicose estão alarmantes, possível quadro de Diabetes.')
    }
}