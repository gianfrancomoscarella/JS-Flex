import { Router } from './modules/router.js';
import { Paginas } from './modules/pages.js';
import { Navegacion } from './modules/navigation.js';

class MiSPA {
    constructor() {
        this.router = new Router();
        this.paginas = new Paginas();
        this.navegacion = new Navegacion();
        this.configurar();
    }

    configurar() {
        this.configurarRutas();
        this.navegacion.router = this.router;
        this.router.iniciar();
    }

    configurarRutas() {
        this.router.agregarRuta('inicio', () => this.paginas.mostrarInicio());
        this.router.agregarRuta('acerca', () => this.paginas.mostrarAcerca());
        this.router.agregarRuta('contacto', () => this.paginas.mostrarContacto());
        this.router.agregarRuta('tienda', () => this.paginas.mostrarTienda());
        this.router.agregarRuta('*', () => this.router.irA('inicio'));
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const app = new MiSPA();
    window.miApp = app;
});
