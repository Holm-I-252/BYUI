const pokemon = document.querySelectorAll("li");
      const displayPokemon = document.getElementById("display_pokemon");

      let activePokemon = "";

      function search(){
        let input = document.getElementById('search').value
        input=input.toLowerCase();

        let url = `https://pokeapi.co/api/v2/pokemon/${input}`;

          console.log(url);

          fetch(url)
            .then((response) => {
              if (!response.ok) {
                throw new Error("Network response was not ok");
              }
              return response.json();
            })
            .then((data) => {
              console.log(data);

              let type = document.getElementById("type");
              if (data.types.length > 1) {
                type.innerHTML = `<h3>Type: ${data.types[0].type.name} / ${data.types[1].type.name}</h3>`;
              } else {
                type.innerHTML = `<h3>Type: ${data.types[0].type.name}</h3>`;
              }

              let hp = document.getElementById("hp");
              hp.innerHTML = `<h3>HP: ${data.stats[0].base_stat}</h3>`;

              let attack = document.getElementById("attack");
              attack.innerHTML = `<h3>Attack: ${data.stats[1].base_stat}</h3>`;

              let defense = document.getElementById("defense");
              defense.innerHTML = `<h3>Defense: ${data.stats[2].base_stat}</h3>`;

              let specialAttack = document.getElementById("special-attack");
              specialAttack.innerHTML = `<h3>Special Attack: ${data.stats[3].base_stat}</h3>`;

              let specialDefense = document.getElementById("special-defense");
              specialDefense.innerHTML = `<h3>Special Defense: ${data.stats[4].base_stat}</h3>`;

              let speed = document.getElementById("speed");
              speed.innerHTML = `<h3>Speed: ${data.stats[5].base_stat}</h3>`;

              let id = data.id;
              console.log(id);
              
              if (data.id < 151){
                  displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/red-blue/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
                } else if (data.id < 251){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/crystal/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else if (data.id < 386){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/ruby-sapphire/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else if (data.id < 494){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/black-white/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else if (data.id < 650){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/black-white/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else if (data.id < 722){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/black-white/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else if (data.id < 810){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/black-white/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else if (data.id < 1000){
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/black-white/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } else {
                displayPokemon.innerHTML = `<div class="active"><img src="https://img.pokemondb.net/sprites/black-white/normal/${input}.png" alt="${input}"/>${input}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div></div>`;
            } 

            activePokemon = input;

            input = "";

            document.getElementById("show_moves").addEventListener("click", showMoves);
        })
            .catch((error) => {
              console.error("Error fetching data from the API: ", error);
            });

      }

      document.getElementById("search_btn").addEventListener("click", search);

      pokemon.forEach((poke) => {
        poke.addEventListener("click", () => {
          displayPokemon.innerHTML = `<div class="active">${poke.innerHTML}<button id="show_moves">Show Level-Up Moves</button><div id="moves"></div><button id="show_abilities">Show Abilities</button><div id="abilities"></div></div>`;

          let url = `https://pokeapi.co/api/v2/pokemon/${poke.innerText.toLowerCase()}`;
          activePokemon = poke.innerText.toLowerCase();
          
          document.getElementById("show_moves").addEventListener("click", showMoves);
          document.getElementById("show_abilities").addEventListener("click", showAbilities);
          
          console.log(url);

          fetch(url)
            .then((response) => {
              if (!response.ok) {
                throw new Error("Network response was not ok");
              }
              return response.json();
            })
            .then((data) => {
              console.log(data);
              
              let type = document.getElementById("type");
              if (data.types.length > 1) {
                type.innerHTML = `<h3>Type: ${data.types[0].type.name} / ${data.types[1].type.name}</h3>`;
              } else {
                type.innerHTML = `<h3>Type: ${data.types[0].type.name}</h3>`;
              }

              let hp = document.getElementById("hp");
              hp.innerHTML = `<h3>HP: ${data.stats[0].base_stat}</h3>`;

              let attack = document.getElementById("attack");
              attack.innerHTML = `<h3>Attack: ${data.stats[1].base_stat}</h3>`;

              let defense = document.getElementById("defense");
              defense.innerHTML = `<h3>Defense: ${data.stats[2].base_stat}</h3>`;

              let specialAttack = document.getElementById("special-attack");
              specialAttack.innerHTML = `<h3>Special Attack: ${data.stats[3].base_stat}</h3>`;

              let specialDefense = document.getElementById("special-defense");
              specialDefense.innerHTML = `<h3>Special Defense: ${data.stats[4].base_stat}</h3>`;

              let speed = document.getElementById("speed");
              speed.innerHTML = `<h3>Speed: ${data.stats[5].base_stat}</h3>`;
            })
            .catch((error) => {
              console.error("Error fetching data from the API: ", error);
            });

          window.scrollTo({
            top: 0,
            behavior: "smooth",
          });
        });
      });

      function showMoves(){
        document.getElementById("show_moves").remove();
        let url = `https://pokeapi.co/api/v2/pokemon/${activePokemon}`;

        fetch(url)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            console.log(data);

            let moves = document.getElementById("moves");

            data.moves.forEach((move) => {
              if (move.version_group_details[0].move_learn_method.name == "level-up") {
                moves.innerHTML += `<p class="move">${move.move.name}: lvl ${move.version_group_details[0].level_learned_at},</p>`;
              }
            });
          })
          .catch((error) => {
            console.error("Error fetching data from the API: ", error);
          });
      }

      function showAbilities(){
        document.getElementById("show_abilities").remove();
        let url = `https://pokeapi.co/api/v2/pokemon/${activePokemon}`;

        fetch(url)
          .then((response) => {
            if (!response.ok) {
              throw new Error("Network response was not ok");
            }
            return response.json();
          })
          .then((data) => {
            console.log(data);

            let abilities = document.getElementById("abilities");

            abilities.innerHTML += `<h3 id="ability_info">Green = Not hidden, Red = Hidden</h3><div id="ability_container"></div>`;

            data.abilities.forEach((ability) => {
              if (ability.is_hidden == false) {
                document.getElementById("ability_container").innerHTML += `<p class="ability" id="not_hidden">${ability.ability.name}</p>`;
              }
              else {
                document.getElementById("ability_container").innerHTML += `<p class="ability" id="hidden">${ability.ability.name}</p>`;
              }
            });
          })
          .catch((error) => {
            console.error("Error fetching data from the API: ", error);
          });
      }