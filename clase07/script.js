const btn = document.querySelector("#btn")
const btnFondo = document.querySelector("#btn-fondo")
const btnAzul = document.querySelector("#btn-azul")
const parrafo = document.querySelector('#parrafo')
const imagen = document.querySelector('img')

const campoTexto = document.querySelector("input[type='text']")
const papel = document.querySelector('#papel')

const btnIngresar = document.querySelector('#btn-ingresar')

btn.addEventListener("click", () => {
    parrafo.textContent = "Texto cambiado"
})


btnFondo.addEventListener("click",()=> {
    parrafo.style.backgroundColor = "yellow"
})

parrafo.addEventListener("mouseenter", () => {
    parrafo.style.backgroundColor = "yellow";
        parrafo.style.cursor = "pointer";
});

parrafo.addEventListener("mouseleave", () => {
    parrafo.style="";
});

btnAzul.onclick = () => {
    //alert()
    parrafo.style.backgroundColor = "blue"
}

/* campoTexto.addEventListener("input",()=>{
    console.log(campoTexto.value)
    papel.textContent = campoTexto.value
}) */


btnIngresar.addEventListener("click",()=>{
    papel.textContent = campoTexto.value
    imagen.src =
      "https://e01-phantom-elmundo.uecdn.es/b7043650c171a6cfc6a65644e34cff64/resize/1200/f/webp/assets/multimedia/imagenes/2024/04/10/17127518856147.png";
})
