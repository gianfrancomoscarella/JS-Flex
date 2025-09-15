const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Diciembre"]

const carrito = [
    {nombre: "Camisa", precio: 50, cantidad: 2},
    {nombre: "Pantalon", precio: 80, cantidad: 10},
    {nombre: "Zapatos", precio: 120, cantidad: 6},
];

/*const existe = meses.includes("Diciembre")
console.log(existe)*/

/*const existe2 = meses.some((mes)=>{return mes === "Diciembre"})
console.log(existe2)*/

const existeEnCarritoCantidad = carrito.some(item => item.cantidad >= 1)
const existeEnCarritoNombre = carrito.some(item => item.nombre == "Pelota")
console.log(existeEnCarritoCantidad)
console.log(existeEnCarritoNombre)
