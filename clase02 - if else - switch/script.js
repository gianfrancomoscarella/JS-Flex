let rol = prompt("Ingrese rol de usuario: Admin, Editor, otro. ")

if(rol === "Admin"){
    console.log("El usuario puede hacer todo")
} else if (rol === "Editor"){
    console.log("solo puede editar")
} else {
   console.log("El usuario no puede hacer nada")
}

let metodoPago = prompt("Ingrese metodo de pago: Efectivo, Tarjeta, MercadoPago")