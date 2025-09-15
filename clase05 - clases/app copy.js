function Cliente(primero, segundo){
    this.nombre = primero,
    this. saldo = segundo,
    this.saludo = function(){
        console.log("Hola")
    },
    this.saludoPersonalizado = function(){
        console.log(`Hola, mi nombre ${this.nombre} y tengo ${this.saldo}`)
    },
    this.retirarDinero = function(){}
    this.depositar = function(){}
}

Cliente.prototype.tipoCliente = function(){
    let tipo;
    if(this.saldo > 10000){
        tipo = "Gold"
    }else if(this.saldo > 5000){
        tipo = "Platinum"
    } else {
        tipo = "Normal"
    }
    return tipo;
}

const cliente1 = new Cliente("Raul", 250);
console.log(cliente1)
const cliente2 = new Cliente("Juan", 500);
console.log(cliente2)
const cliente3 = new Cliente("Mateo", 1500);
console.log(cliente3)

console.log(cliente1.saludo)
console.log(cliente1.saludoPersonalizado)
console.log(cliente2.saludo)
console.log(cliente2.saludoPersonalizado)
console.log(cliente3.saludo)
console.log(cliente3.saludoPersonalizado)
