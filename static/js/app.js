/**
 * This function will grab the pokemon generation information from the poke API.
 * @param {int} id 
 * @returns 
 */
async function retrieveGenerationInfo(id){
    try{
        let res = await fetch(`https://pokeapi.co/api/v2/generation/${id}`)
        .then((response) => response.json());
        
        return res.pokemon_species;
    }
    catch(err){
        console.log("ERROR!!!!", err);
    }
}

/**
 * This function will read the URL and extracts the ID from the url.
 * @param {string} url 
 * @returns id in string
 */
function extractIdFromUrl(url){
    return url.slice(42, 45).replace('/', '');
}

/**
 * This function will create elements for the pokemon grid.
 * Appends the name and image to the grid.
 * Appends the grid to the div grid-container.
 * @param {Object} pokemon_dict 
 */
function createGrid(pokemon_dict){
    //Loop over the ordered pokemon dictionary.
    for (let key in pokemon_dict){
        const pokemon_grid_div = document.createElement("div");
        pokemon_grid_div.classList.add('pokemon-list-grid');
        pokemon_grid_div.style.margin = "auto";


        const pokemon_image_anchor = document.createElement("a");
        pokemon_image_anchor.style.display = "block";
        pokemon_image_anchor.href = `/pokemon/add_or_info/${key}/get`;
        
        const pokemon_image_div = document.createElement("div");

        const img_tag = document.createElement("img");
        img_tag.src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${key}.png`
        img_tag.style.height = '250px';
        img_tag.style.width = '250px';

        pokemon_image_div.append(img_tag);
        pokemon_image_anchor.append(pokemon_image_div);
        pokemon_grid_div.append(pokemon_image_anchor);
        

        //Create div container for pokemon name and image.
        //Appends the name and image to the div container
        //Create an anchor tag that references python route.
        //Appends anchor tag to the grid-item div.
        const pokemon_name_div = document.createElement("div");
        pokemon_name_div.classList.add("pokemon-name-div");
        pokemon_name_div.append(pokemon_dict[key]);
        pokemon_grid_div.append(pokemon_name_div);
        
        //Creates a button for the img element for each pokemon.
        //Clicking this button will add the pokemon to the current trainer's team.
        const pokeball_div = document.createElement("div");
        pokeball_div.classList.add("pokeball-div");

        const pokeball_ball_div = document.createElement("div");
        pokeball_ball_div.classList.add("material-icons");

        pokeball_div.append(pokeball_ball_div);

        const pokeball_ball_anchor = document.createElement("a");
        pokeball_ball_anchor.innerText = "catching_pokemon";
        pokeball_ball_anchor.classList.add('pokeball-anchor-button');
        pokeball_ball_anchor.href = `/pokemon/add_or_info/${key}/post`;

        pokeball_ball_div.append(pokeball_ball_anchor);
        pokemon_grid_div.append(pokeball_div)

        $('.pokemon-div-wrapper').append(pokemon_grid_div);
    }
}

$(document).ready(async function(){
    const pokemon_species = await retrieveGenerationInfo(1);

    let pokemon_dict = {};

    for(let i = 0; i < pokemon_species.length; i++){

        //Emptys the pokemon section when another gen button is clicked.
        $('.pokemon-div-wrapper').empty();

        //Extracts the id from the URL.
        // id will serve for retrieving pokemon images.
        let id = extractIdFromUrl(pokemon_species[i].url);
        let num = "";

        for(let j = 0; j < id; j ++){
            if(!isNaN(id[j])){
                num = num + id[j];
            }
        }  
        pokemon_dict[num] = pokemon_species[i].name.toUpperCase();
    }
    createGrid(pokemon_dict);
    $('.pokemon-gen-container a:first-child').addClass('active-gen-button disabled');
})

/**
 * Event button for each pokemon generations.
 * Clicking a button will retrieve the information from pokemon API.
 * It will create elements and dynamically adds onto the page.
 */

$('.pokemon-gen-container').on('click', '.gen-button', async function(e){
    e.preventDefault();
    $(this).addClass('active-gen-button disabled').siblings().removeClass('active-gen-button disabled');

    $(".pokemon-list-flash").hide();

    const pokemon_species = await retrieveGenerationInfo(e.target.id);
    let pokemon_dict = {};

    for(let i = 0; i < pokemon_species.length; i++){

        //Emptys the pokemon section when another gen button is clicked.
        $('.pokemon-div-wrapper').empty();

        //Extracts the id from the URL.
        // id will serve for retrieving pokemon images.
        let id = extractIdFromUrl(pokemon_species[i].url);
        let num = "";

        for(let j = 0; j < id; j ++){
            if(!isNaN(id[j])){
                num = num + id[j];
            }
        }  
        pokemon_dict[num] = pokemon_species[i].name.toUpperCase();
    }
    createGrid(pokemon_dict);

    $(".pokeball-anchor-button").hover(
        function() { 
            $(this).prepend("<span style='position: absolute; font-size: 14px; border: 1px solid black; border-radius: 50%; margin: -12px 0 0 40px; padding: 9px; font-family: Orbitron, sans-serif;'>Capture</span>");
        }, function() {
            $(this).find("span").remove();
        }
    );
})


$(".left-profile-box-grid").hover(
        function() { 
            $(this).animate({
                opacity: '0.3',
                color: '#7F8487'
            }, "slow");

            $(this).parent().prepend("<span style='position: absolute; font-size: 20px; border: 1px solid black; border-radius: 50%; margin: -30px -45px 0 0; padding: 10px; font-family: Orbitron, sans-serif;'>Release</span>");
        }, function() {
            $(this).animate({
                opacity: '1' 
            }, "slow");

            $(this).parent().find("span").remove();
        }
    );