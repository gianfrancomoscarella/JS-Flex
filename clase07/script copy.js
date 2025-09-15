//alert()
/* let miVariable = document.body
console.log(miVariable)
console.log(typeof miVariable)


document.querySelector('h1').textContent = 'Hola Mundo' */
let contenedor = document.querySelector('div')
/* let h1 = document.querySelector('h1')
h1.textContent = "La mejor pagina del mundo"
document.querySelector('h1').textContent = 'Raul Auad'
h1.style.color = "yellow";
h1.style.color = 'red'
let img = document.querySelector('img')
img.src =
  "https://www.semana.com/resizer/v2/YI37KOOP2ZBMBJ3ZFPLBKOGABM.jpg?auth=c19d94947a96415068aaa4d3f1fc6fb6824edf525d457f0049429fc47b2a5909&smart=true&quality=75&width=1280&height=1280";
img.width = "300";
console.log(contenedor) */
//contenedor.textContent = "<h2>Este es el titulo del contenedor</h2>"

const producto = {
  title: "Los Simpson",
  description: "La mejor serie de todos los tiempos",
  img: "https://www.semana.com/resizer/v2/YI37KOOP2ZBMBJ3ZFPLBKOGABM.jpg?auth=c19d94947a96415068aaa4d3f1fc6fb6824edf525d457f0049429fc47b2a5909&smart=true&quality=75&width=1280&height=1280",
};

contenedor.innerHTML = `
  <img src="${producto.img}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${producto.title}</h5>
    <p class="card-text">${producto.description}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
`;
