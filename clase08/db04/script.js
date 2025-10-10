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


async function loadCharacters(){
    //console.log("ya se cargo el dom")
    //console.log("Cargando datos")
    //console.log("viendo la que tiene el json")
    const container = document.querySelector("#characters-container");
    const error = document.querySelector("#error-message");
    const loading = document.getElementById("loading")

    error.style.display = "none";
    container.style.display = "block";


    try {
    const response = await fetch(API_URL) // tarda
    loading.style.display = "block"
    if(!response.ok){
        throw new Error("Error " + response.status)
    }
    const data = await response.json()
    const characters = data.items
    container.innerHTML = characters
    .map(character => createCharacterCard(character))
    .join('')
    
    } catch (err) {
        error.style.display = "block";
        container.style.display = "none";
        document.querySelector("#error-text").innerText = err.message;
    } finally{
        loading.style.display = "none";
    }
}


//document.addEventListener('DOMContentLoaded', loadCharacters)
setTimeout(loadCharacters, 2000);
