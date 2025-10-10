// Router simple - maneja las páginas
export class Router {
    constructor() {
        this.rutas = {};
        this.paginaActual = 'inicio';
    }

    agregarRuta(nombre, funcion) {
        this.rutas[nombre] = funcion;
    }

    irA(nombrePagina) {
        if (this.rutas[nombrePagina]) {
            window.location.hash = nombrePagina;
            if (this.obtenerPaginaActual() === nombrePagina) {
                this.cambiarPagina(nombrePagina);
            }
        } else {
            console.log('Página no encontrada:', nombrePagina);
            if (nombrePagina !== 'inicio') this.irA('inicio');
        }
    }

    obtenerPaginaActual() {
        const hash = window.location.hash.replace('#', '');
        return hash || 'inicio';
    }

    iniciar() {
        window.addEventListener('hashchange', () => {
            const pagina = this.obtenerPaginaActual();
            if (pagina !== this.paginaActual) {
                this.cambiarPagina(pagina);
            }
        });
        const paginaInicial = this.obtenerPaginaActual();
        this.cambiarPagina(paginaInicial);
    }

    cambiarPagina(nombrePagina) {
        if (this.rutas[nombrePagina]) {
            this.paginaActual = nombrePagina;
            this.rutas[nombrePagina]();
            if (window.miApp && window.miApp.navegacion) {
                setTimeout(() => {
                    window.miApp.navegacion.actualizarMenuActivo();
                }, 10);
            }
        } else if (this.rutas['*']) {
            this.rutas['*']();
        }
    }
}
