# Tutorial: Carrusel de Imágenes en JavaScript, HTML y CSS

Este tutorial te guiará paso a paso para crear un carrusel de imágenes simple utilizando HTML, CSS y JavaScript. El ejemplo se encuentra en esta misma carpeta.

## Archivos del proyecto

- `index.html`: Estructura HTML del carrusel.
- `style.css`: Estilos para el carrusel y las imágenes.
- `script.js`: Lógica para el funcionamiento del carrusel.
- Carpeta `assets/`: Imágenes utilizadas en el carrusel.

## 1. Estructura HTML (`index.html`)

El archivo HTML contiene un contenedor principal para el carrusel y los botones de navegación:

```html
<div class="carrusel">
  <button id="prev">&#10094;</button>
  <img id="imagen-carrusel" src="assets/esfera1.png" alt="Imagen Carrusel">
  <button id="next">&#10095;</button>
</div>
```

## 2. Estilos CSS (`style.css`)

El CSS centra el carrusel y da estilo a los botones y la imagen:

```css
.carrusel {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}
.carrusel img {
  width: 300px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.carrusel button {
  background: #fff;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  padding: 0.5rem 1rem;
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: background 0.2s;
}
.carrusel button:hover {
  background: #eee;
}
```

## 3. Lógica JavaScript (`script.js`)

El JavaScript permite cambiar de imagen al hacer clic en los botones. Asegúrate de que el archivo `script.js` contenga una lógica similar a la siguiente:

```js
const imagenes = [
  'assets/esfera1.png',
  'assets/esfera2.png',
  'assets/esfera3.png',
  'assets/esfera4.png',
  'assets/esfera5.png',
  'assets/esfera7.png'
];

let indice = 0;
const img = document.getElementById('imagen-carrusel');

if (img && document.getElementById('prev') && document.getElementById('next')) {
  document.getElementById('prev').onclick = () => {
    if (imagenes.length === 0) return;
    indice = (indice - 1 + imagenes.length) % imagenes.length;
    img.src = imagenes[indice];
  };

  document.getElementById('next').onclick = () => {
    if (imagenes.length === 0) return;
    indice = (indice + 1) % imagenes.length;
    img.src = imagenes[indice];
  };
} else {
  // Si el DOM aún no está listo, envolver en DOMContentLoaded
  document.addEventListener('DOMContentLoaded', () => {
    const imgEl = document.getElementById('imagen-carrusel');
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');
    if (!imgEl || !prev || !next) return;
    prev.onclick = () => {
      if (imagenes.length === 0) return;
      indice = (indice - 1 + imagenes.length) % imagenes.length;
      imgEl.src = imagenes[indice];
    };
    next.onclick = () => {
      if (imagenes.length === 0) return;
      indice = (indice + 1) % imagenes.length;
      imgEl.src = imagenes[indice];
    };
  });
}
```

## 4. Personalización

- Puedes agregar más imágenes a la carpeta `assets/` y al arreglo `imagenes` en `script.js`.
- Modifica los estilos en `style.css` para cambiar el diseño del carrusel.
- Para añadir controles de paginación (puntos) o autoplay, amplía la lógica con timers y elementos extra en HTML.

## 5. Vista previa

Abre `index.html` en tu navegador para ver el carrusel en acción.

---

¡Listo! Ahora tienes un carrusel funcional y personalizable.

## Explicación técnica del JavaScript

A continuación se detalla la lógica usada en `script.js` y recomendaciones técnicas:

- Arreglo de imágenes: `const imagenes = [...]` contiene rutas relativas a la carpeta `assets/`.
- Índice actual: `let indice = 0;` mantiene la posición de la imagen mostrada.
- Elemento `img`: `const img = document.getElementById('imagen-carrusel')` se usa para actualizar `src`.
- Manejo de eventos: se registran manejadores en `prev` y `next` que actualizan `indice` y asignan `img.src`.
- Ciclo circular: el operador módulo garantiza que el índice envuelva dentro del rango válido:

```js
indice = (indice + 1) % imagenes.length; // siguiente
indice = (indice - 1 + imagenes.length) % imagenes.length; // anterior
```

- Buenas prácticas y recomendaciones:
  - Comprueba que los elementos existen antes de acceder a ellos para evitar errores si el script se ejecuta antes que el DOM.
  - Usa `<script src="script.js" defer></script>` o coloca el `<script>` al final del `body` para cargar el script después del DOM.
  - Valida `imagenes.length > 0` antes de actualizar `src`.
  - Para transiciones suaves, aplica `opacity` y `transition` en CSS o controla la animación desde JavaScript.
  - Considera separar la lógica en funciones reutilizables (inicializar, irSiguiente, irAnterior) para facilitar pruebas y mantenimiento.

Con esto dispones de una explicación técnica clara para entender y extender la funcionalidad del carrusel.
