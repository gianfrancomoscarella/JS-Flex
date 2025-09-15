const carrito = [
    {nombre: "Camisa", precio: 50, cantidad: 2},
    {nombre: "Pantalon", precio: 80, cantidad: 10},
    {nombre: "Zapatos", precio: 120, cantidad: 5},
];

const resultado = carrito.every (item => item.precio >20)
console.log(resultado)