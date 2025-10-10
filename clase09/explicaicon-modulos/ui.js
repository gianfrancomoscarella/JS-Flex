


export function createButton(){
    console.log("dibujar un boton")
}

export const PI = 3.1416;

export class Circulo {
    constructor(radio) {
        this.radio = radio;
    }

    area() {
        return PI * this.radio ** 2;
    }
}
