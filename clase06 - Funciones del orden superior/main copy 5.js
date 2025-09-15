const carrito = [
    {nombre: "Camisa", precio: 50, cantidad: 1},
    {nombre: "Pantalon", precio: 80, cantidad: 2},
    {nombre: "Zapatos", precio: 120, cantidad: 1},
];

let total = 0;
carrito.forEach(item => total += item.precio * item.cantidad)
console.log(total)

const resultado = carrito.reduce((total, item) => total + (item.precio * item.cantidad),0)
console.log(resultado)

