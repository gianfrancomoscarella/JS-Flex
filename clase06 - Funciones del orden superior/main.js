let marca = prompt("Ingrese Marca");
let year = parseInt(prompt("Ingrese Año"));
let minimo = Number(prompt("Ingrese minimo"));
let maximo = Number(prompt("Ingrese maximo"));

const datosBusqueda = {
  marca: marca,
  year: year,
  minimo: minimo,
  maximo: maximo,
  puertas: "",
};

function mostrarAutos(autos) {
  autos.forEach((auto) => {
    console.log(
      `Marca: ${auto.marca}, Modelo: ${auto.modelo}, Año: ${auto.year}, Precio: ${auto.precio}, Puertas: ${auto.puertas}, Color: ${auto.color}, Transmisión: ${auto.transmision}`
    );
  });
}

function filtrarMarca(auto) {
  if (datosBusqueda.marca) {
    return auto.marca === datosBusqueda.marca;
  }
  return auto;
}

function filtrarYear(auto) {
  if (datosBusqueda.year) {
    return auto.year === datosBusqueda.year;
  }
  return auto;
}

function filtarMinimo(auto) {
  if (datosBusqueda.minimo) {
    return auto.precio >= datosBusqueda.minimo;
  } else {
    return auto;
  }
}

function filtrarMaximo(auto) {
  if (datosBusqueda.maximo) {
    return auto.precio <= datosBusqueda.maximo;
  } else {
    return auto;
  }
}

function filtrarPuertas(auto) {
  if (datosBusqueda.puertas) {
    return auto.puertas === datosBusqueda.puertas;
  } else {
    return auto;
  }
}

function filtrarAutos() {
  const resultado = autos
    .filter(filtrarMarca)
    .filter(filtrarYear)
    .filter(filtarMinimo)
    .filter(filtrarMaximo)
    .filter(filtrarPuertas);
  mostrarAutos(resultado);
}

filtrarAutos();
//mostrarAutos(autos);