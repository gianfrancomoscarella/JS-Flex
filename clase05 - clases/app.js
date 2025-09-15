console.log(localStorage)
localStorage.setItem("nombre", "Noelia")
localStorage.setItem("edad", 30)
localStorage.setItem("estudia", true)
localStorage.setItem("cursos", ["Web", "JavaScript"])
localStorage.setItem("datos", {id: 123445, presentismo: true})

sessionStorage.setItem("nombre", "Noelia")
sessionStorage.setItem("edad", 30)
sessionStorage.setItem("estudia", true)
sessionStorage.setItem("cursos", ["Web", "JavaScript"])
sessionStorage.setItem("datos", {id: 123445, presentismo: true})

let nombre = localStorage.getItem("Nombre");
let edad = parseFloat(localStorage.getItem("Edad"));
let estudia = localStorage.getItem("Estudia") === true;
let cursos = localStorage.getItem("cursos").split(",");
let datos = JSON.parse(localStorage.getItem("datos"));

console.log(nombre)
console.log(edad)
console.log(estudia)
console.log(cursos)
console.log(datos)