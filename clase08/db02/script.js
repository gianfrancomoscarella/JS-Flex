const API_URL = "https://dragonball-api.com/api/characters";


function createCharacterCard(character){
    return `
        <div class="character-card">
            <img class="character-image" src="${character.image}" alt="${character.name}"/>
            <h3 class="character-name">${character.name}</h3>
            <div>
                ${
                    character.race
                ? `<div class='character-info'><span class='info-label'>Raza: </span><span class='info-value race-tag'>${character.race}</span></div>`
                : ''
                }
                ${
                    character.gender
                    ? `<div class='info-item'><span class='info-label'>Genero: </span><span class='info-value race-tag'>${character.gender}</span></div>`
                    : ''
                }
            </div>
        </div>
    `
}


function loadCharacters(){
    //console.log("ya se cargo el dom")
    //console.log("Cargando datos")
    //console.log("viendo la que tiene el json")
    const container = document.querySelector("#characters-container");

    fetch(API_URL)
    .then((res)=>{
        console.log(res);
        if(!res.ok){
            throw new Error("Error " + res.status)
        }
        return res.json();
    })
    .then((datos)=>{
        //console.log(datos.items);
        // dibujar los datos en el html 
        const characters = datos.items;
        container.innerHTML = characters.map((character) =>
          createCharacterCard(character)
        );
        
    })
    .catch((error)=>{
        console.log("no se pudo cargar el json", error)
    })

}


//document.addEventListener('DOMContentLoaded', loadCharacters)
loadCharacters()
