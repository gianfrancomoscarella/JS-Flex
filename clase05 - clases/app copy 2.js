class Cliente{
    constructor(n, s){
        this.nombre = n;
        this.saldo = s;
    }

    consultarSaldo() {
        return `Hola ${this.nombre}, tu saldo es ${this.saldo}`
    }

    retirarSaldo(cantidad) {
        this.saldo -= cantidad
    }

    static bienvenida(){
        return "Bienvenido a nuestro banco"
    }
}

let cliente1 = new Cliente ("Ali", 500)
let cliente2 = new Cliente("Renzo", 1500)

console.log(cliente1);

console.log(cliente1.nombre);
console.log(cliente1.consultarSaldo())
cliente1.retirarSaldo(100)
console.log(cliente1.consultarSaldo())
console.log(cliente2.consultarSaldo())
