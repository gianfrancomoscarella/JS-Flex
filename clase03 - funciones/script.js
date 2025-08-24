const MIN_POWER = 10;
const MAX_POWER = 30;

let energiaGoku = 100;
let energiaSuperman = 100;

let round = 0;

while(energiaGoku > 0 && energiaSuperman > 0){

    round++;
    console.log("Round: " + round)
let golpeGoku = parseInt(Math.random() * (MAX_POWER - MIN_POWER) + MIN_POWER);
let golpeSuperman = parseInt(Math.random() * (MAX_POWER - MIN_POWER) + MIN_POWER);

if(golpeGoku == golpeSuperman){
    console.log("Empate")
} else if (golpeGoku > golpeSuperman){
    console.log("Goku golpea con una fuerza de " + golpeGoku)
    energiaSuperman -= golpeGoku
} else {
    console.log("Superman golpea con una fuerza de " + golpeSuperman)
    energiaGoku -= golpeSuperman
}

if (energiaGoku > energiaSuperman){
    console.log("Ganador: Goku")
} else {
    console.log("Ganador: Superman")
}
console.log("-------------------------------------------------")
}