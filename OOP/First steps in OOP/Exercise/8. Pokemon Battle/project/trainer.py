from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        # curr_pokemon = Pokemon(pokemon)
        if pokemon.pokemon_details() not in self.pokemons:
            self.pokemons.append(pokemon.pokemon_details())
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for pok in self.pokemons:
            if pokemon_name in pok:
                deleted = self.pokemons.pop(self.pokemons.index(pok))
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n'
        for pokemon in self.pokemons:
            result += f'- {pokemon}\n'
        return result

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())