// Navegación - manejo del menú y enlaces
export class Navegacion {
    constructor() {
        this.menu = document.getElementById('menu');
        this.configurarEventos();
    }

    configurarEventos() {
        if (!this.menu) return;
        const enlaces = this.menu.querySelectorAll('a');
        enlaces.forEach(enlace => {
            enlace.addEventListener('click', (e) => {
                e.preventDefault();
                const nuevaPagina = enlace.getAttribute('href').replace('#', '');
                this.irAPagina(nuevaPagina);
            });
        });
    }

    irAPagina(pagina) {
        if (this.router) this.router.irA(pagina);
        else if (window.miApp && window.miApp.router) window.miApp.router.irA(pagina);
        else window.location.hash = pagina;
        setTimeout(() => this.actualizarMenuActivo(), 10);
    }

    actualizarMenuActivo() {
        const paginaActual = window.location.hash.replace('#', '') || 'inicio';
        const enlaces = this.menu.querySelectorAll('a');
        enlaces.forEach(enlace => enlace.classList.remove('active'));
        enlaces.forEach(enlace => {
            const hrefPagina = enlace.getAttribute('href').replace('#', '');
            if (hrefPagina === paginaActual) enlace.classList.add('active');
        });
    }
}
