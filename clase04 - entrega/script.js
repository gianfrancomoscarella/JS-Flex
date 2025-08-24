let listaCanciones = [];

const isAlpha = str => /^[A-Za-zÁÉÍÓÚÜáéíóúüÑñ\s]+$/.test(str);

function validarTitulo() {
    const titulo = prompt("Ingrese el título");
    if (isAlpha(titulo) && titulo.length > 4) {
        return titulo.trim();
    } else {
        alert("Título inválido, reingrese el título");
        return validarTitulo();
    }
}

function validarArtista() {
    const artista = prompt("Ingrese el artista");
    if (isAlpha(artista) && artista.length >= 2) {
        return artista.trim();
    } else {
        alert("Artista inválido, reingrese el artista");
        return validarArtista();
    }
}

const isDuracion = str => /^\d+:[0-5]\d$/.test(str);

function validarDuracion() {
    const duracion = prompt("Ingrese la duración");
    if (isDuracion(duracion)) {
        return duracion.trim();
    } else {
        alert("Duración inválida, reingrese la duración");
        return validarDuracion();
    }
}

function agregarCancion() {
    const titulo = validarTitulo();
    const artista = validarArtista();
    const duracion = validarDuracion();

    listaCanciones.push({ titulo, artista, duracion });
    alert("Canción agregada correctamente");
}

function mostrarListaCanciones() {
    if (listaCanciones.length === 0) {
        alert("No hay canciones guardadas");
    } else {
        let texto = "Canciones guardadas:\n";
        listaCanciones.forEach((c, i) => {
            texto += `${i + 1}. ${c.titulo} - ${c.artista} (${c.duracion})\n`;
        });
        alert(texto);
    }
}

function buscarCancionPorTitulo() {
    const tituloBuscado = prompt("Ingrese el título de la canción a buscar:");
    const cancion = listaCanciones.find(c => c.titulo.toLowerCase() === tituloBuscado.toLowerCase());

    if (cancion) {
        alert(`Canción encontrada:\nTítulo: ${cancion.titulo}\nArtista: ${cancion.artista}\nDuración: ${cancion.duracion}`);
    } else {
        alert("Canción no encontrada");
    }
}

function mostrarCancionesLargas() {
    const cancionesLargas = listaCanciones.filter(c => {
        const partes = c.duracion.split(":");
        const segundosTotales = parseInt(partes[0]) * 60 + parseInt(partes[1]);
        return segundosTotales > 300; // más de 5 minutos
    });

    if (cancionesLargas.length === 0) {
        alert("No hay canciones largas (>5 min)");
    } else {
        let texto = "Canciones largas (>5 min):\n";
        cancionesLargas.forEach(c => {
            texto += `${"Titulo: " + c.titulo} - ${"Artista: " + c.artista} ${"Duracion: " + c.duracion}\n`;
        });
        alert(texto);
    }
}

function confirmacionSalir() {
    const confirmacion = confirm("¿Estás seguro de que quieres salir?");
    if (confirmacion) {
        alert("Saliendo...");
    }
}

function menuCanciones() {
    let opcion;
    do {
        opcion = prompt(
            "Canciones\n" +
            "1. Agregar canción\n" +
            "2. Mostrar lista de canciones\n" +
            "3. Buscar canción por título\n" +
            "4. Mostrar canciones largas (>5 min)\n" +
            "5. Salir"
        );

        switch (opcion) {
            case "1":
                agregarCancion();
                break;
            case "2":
                mostrarListaCanciones();
                break;
            case "3":
                buscarCancionPorTitulo();
                break;
            case "4":
                mostrarCancionesLargas();
                break;
            case "5":
                confirmacionSalir();
                break;
            default:
                alert("Opción no válida");
        }
    } while (opcion !== "5");
}

menuCanciones();
