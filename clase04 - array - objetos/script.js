let cancionesObjetos = [];

function agregarCancionObjeto(){
    console.log("agregarCancionObjetos");
    const titulo = prompt("Ingrese el titulo")
    const artista = prompt("Ingrese el artista")
    const duracion = prompt("Ingrese la duracion")
    if(titulo && artista && !isNaN(duracion)){
        cancionesObjetos.push({titulo, artista, duracion})
        alert("Cancion agregada")
    }
}
function mostrarListaCanciones(){
    console.log("mostrarListaCanciones");
}
function buscarCancionPorTitulo(){
    console.log("buscarCancionPorTitulo");
}
function mostrarCancionesLargas(){
    console.log("mostrarCancionesLargas");
}

function menuObjetos(){
    let opcion
    do {
        opcion = prompt(
            "Canciones como Objetos\n"+
            "1. Agregar cancion\n" +
            "2. Mostrar lista de canciones\n" +
            "3. Buscar cancion por titulo\n" +
            "4. Mostrar canciones largas (>300s)\n" +
            "5. Salir"
        );
        switch(opcion){
            case "1":
                agregarCancionObjeto();
                break
            case "2":
                mostrarListaCanciones();
                break
            case "3":
                buscarCancionPorTitulo();
                break
            case "4":
                mostrarCancionesLargas();
                break
            case "5":
                alert("Saliendo...")
                break
            default:
                alert("Opcion no valida")
        }
    }while (opcion != "5")
}   

menuObjetos()