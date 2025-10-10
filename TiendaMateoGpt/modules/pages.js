// Páginas - contenido de cada página
export class Paginas {
    constructor() {
        this.contenedor = document.getElementById('contenido');
    }

    mostrar(contenidoHTML) {
        if (this.contenedor) {
            this.contenedor.innerHTML = `<div class="pagina">${contenidoHTML}</div>`;
        }
    }

    mostrarInicio() {
        const contenido = `
            <h2>¡Bienvenido a Mi SPA!</h2>
            <p>Esta es una Single Page Application (SPA) muy simple.</p>
            <ul>
                <li>✅ Las páginas cambian sin recargar el navegador</li>
                <li>✅ Es más rápida que un sitio web tradicional</li>
                <li>✅ Ofrece una mejor experiencia al usuario</li>
                <li>✅ Está hecha con HTML, CSS y JavaScript</li>
            </ul>
        `;
        this.mostrar(contenido);
    }

    mostrarAcerca() {
        const contenido = `
            <h2>Acerca de Este Proyecto</h2>
            <ul>
                <li><strong>HTML5:</strong> Estructura</li>
                <li><strong>CSS3:</strong> Estilos</li>
                <li><strong>JavaScript ES6:</strong> Funcionalidad</li>
            </ul>
        `;
        this.mostrar(contenido);
    }

    mostrarContacto() {
        const contenido = `
            <h2>Contacto</h2>
            <p><strong>Email:</strong> contacto@mispa.com</p>
            <p><strong>Teléfono:</strong> +34 123 456 789</p>
        `;
        this.mostrar(contenido);
    }

    mostrarTienda() {
    const contenido = `
        <section id="product-catalog">
            <h2>Nuestros Productos</h2>
            <button id="view-cart-btn">Ver Carrito (<span id="cart-count">0</span>)</button>
            <div id="product-list"></div>
        </section>
    `;
    this.mostrar(contenido);

    import('../script.js')
        .then(mod => {
            mod.inicializarTienda(); // inicializa correctamente cada vez que entras
        })
        .catch(err => console.error("Error al cargar la tienda:", err));
}
}
