/* document.querySelector("h1"); // raro tener muchos h1
document.querySelector("div");
document.querySelector("body"); // no deberia haber mas de 1
document.querySelector("img"); */

// document.querySelector() --> devuelve 1 elemento
// cuando hay muchos solo devuelve el primero

//document.querySelectorAll("h1"); // devuelve todos los h1
//document.querySelectorAll("div"); // devuelve todos los divs
const items = document.querySelectorAll("img"); // devuelve todas las imgs

let lis = document.querySelectorAll("nav ul li")
console.log(lis)
let item2 = document.querySelector("#item2")
console.log(item2)

let impares = document.querySelectorAll(".impar")
console.log(impares)

for(let impar of impares){
    impar.style.backgroundColor = "yellow"
}

for(let item of items) {
    console.log(item)
}
