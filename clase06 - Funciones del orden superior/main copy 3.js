const meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Diciembre"]

function existe(mes){
    if (mes === "Diciembre"){
        console.log("El mes de diciembre existe")
    } else {
        console.log("No se encontro")
    }
}

meses.forEach(function(mes) {
      if (mes === "Diciembre"){
        console.log("El mes de diciembre existe")
    }
})

