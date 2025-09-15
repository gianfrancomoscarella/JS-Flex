let contenedor = document.querySelector("#container");

const producto = {
  title: "Los Simpson",
  description: "La mejor serie de todos los tiempos",
  img: "https://www.semana.com/resizer/v2/YI37KOOP2ZBMBJ3ZFPLBKOGABM.jpg?auth=c19d94947a96415068aaa4d3f1fc6fb6824edf525d457f0049429fc47b2a5909&smart=true&quality=75&width=1280&height=1280",
};



/* contenedor.innerHTML = `
  <img src="${producto.img}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${producto.title}</h5>
    <p class="card-text">${producto.description}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
`; */

let img = document.createElement("img")
img.src = producto.img
img.classList.add("card-img-top")
let cardBody = document.createElement("div")
cardBody.classList.add("card-body")
let h5 = document.createElement("h5")
h5.classList.add("card-title")
h5.textContent = producto.title
let cardText = document.createElement("p")
cardText.classList.add("card-text")
cardText.textContent = producto.description
let btn = document.createElement("a")
btn.classList.add("btn", "btn-primary")
btn.href = "#"
btn.textContent = "Go somewhere"

contenedor.appendChild(img)
contenedor.appendChild(cardBody)
cardBody.appendChild(h5)
cardBody.appendChild(cardText)
cardBody.appendChild(btn)
