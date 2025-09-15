const carrito = [
    {nombre: "Camisa", precio: 50, cantidad: 2},
    {nombre: "Pantalon", precio: 80, cantidad: 10},
    {nombre: "Zapatos", precio: 120, cantidad: 5},
];

let resultado = carrito.filter(item => item.precio > 70)
console.log(resultado)
resultado = carrito.filter(item => item.nombre === "Camisa")
console.log(resultado)
resultado = carrito.filter(item => item.nombre !== "Camisa")
console.log(resultado)