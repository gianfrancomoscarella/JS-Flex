function crearFuncionDeSaludo(tipoSaludo){
    return function(nombre){
        console.log(tipoSaludo + " " + nombre)
    }
}
const sayHello = crearFuncionDeSaludo("Hello")
const decirHola = crearFuncionDeSaludo("Hola")
const sayBye = crearFuncionDeSaludo("Bye")
const decirAdios = crearFuncionDeSaludo("Adios")

decirHola("Mateo")
decirAdios("Juan")