import requests
import json

pokemon_dict = {}
types_dict = {}
moves_dict = {}

def get_pokemon(json_path) :
    request_url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
    all_pokemon = requests.get(request_url).json()
    
    for pokemon in all_pokemon["results"]:
        pokemon_dict[pokemon["name"]] = {}
        request_pokemon = pokemon["url"]
        pokemon_attributes = requests.get(request_pokemon).json()
        pokemon_dict[pokemon["name"]]["type"] = []
        for pokemon_type in pokemon_attributes["types"]:
            pokemon_dict[pokemon["name"]]["type"].append(pokemon_type["type"]["name"])
        pokemon_dict[pokemon["name"]]["moves"] = []
        for move in pokemon_attributes["moves"]:
            pokemon_dict[pokemon["name"]]["moves"].append(move["move"]["name"])
        pokemon_dict[pokemon["name"]]["weight"] = pokemon_attributes["weight"]
        pokemon_dict[pokemon["name"]]["height"] = pokemon_attributes["height"]
        for stat in pokemon_attributes["stats"]:
            if (stat["stat"]["name"] == "speed"):
                pokemon_dict[pokemon["name"]]["speed"] = stat["base_stat"]
                print(stat["base_stat"])
            elif (stat["stat"]["name"] == "attack"):
                pokemon_dict[pokemon["name"]]["attack"] = stat["base_stat"]
            elif (stat["stat"]["name"] == "defense"):
                pokemon_dict[pokemon["name"]]["defense"] = stat["base_stat"]
            elif (stat["stat"]["name"] == "special-attack"):
                pokemon_dict[pokemon["name"]]["special-attack"] = stat["base_stat"]
            elif (stat["stat"]["name"] == "special-defense"):
                pokemon_dict[pokemon["name"]]["special-defense"] = stat["base_stat"]
        pokemon_dict[pokemon["name"]]["img"] = pokemon_attributes["sprites"]["front_default"]

    with open(json_path, "w") as json_file :
        json.dump(pokemon_dict, json_file)

def get_types(json_path) :
    request_url = "https://pokeapi.co/api/v2/type/"
    all_types = requests.get(request_url).json()

    not_gen1_types = ["dark", "steel", "fairy", "shadow"]
    for next_type in all_types["results"]:
        if next_type not in not_gen1_types:
            types_dict[next_type["name"]] = {}
            request_type = next_type["url"]
            type_attributes = requests.get(request_type).json()
            types_dict[next_type["name"]]["half_to"] = []
            types_dict[next_type["name"]]["half_from"] = []
            types_dict[next_type["name"]]["double_to"] = []
            types_dict[next_type["name"]]["double_from"] = []
            for type_affect in type_attributes["damage_relations"]["half_damage_from"]:
                if type_affect not in not_gen1_types:
                    types_dict[next_type["name"]]["half_from"].append(type_affect["name"])
            for type_affect in type_attributes["damage_relations"]["half_damage_to"]:
                if type_affect not in not_gen1_types:
                    types_dict[next_type["name"]]["half_to"].append(type_affect["name"])
            for type_affect in type_attributes["damage_relations"]["double_damage_to"]:
                if type_affect not in not_gen1_types:
                    types_dict[next_type["name"]]["double_to"].append(type_affect["name"])
            for type_affect in type_attributes["damage_relations"]["double_damage_from"]:
                if type_affect not in not_gen1_types:
                    types_dict[next_type["name"]]["double_from"].append(type_affect["name"])
    
    with open(json_path, "w") as json_file:
        json.dump(types_dict, json_file)


def get_moves(json_path) :
    request_url = "https://pokeapi.co/api/v2/move/?limit=165"
    all_moves = requests.get(request_url).json()

    for next_move in all_moves["results"]:
        moves_dict[next_move["name"]] = {}
        request_move = next_move["url"]
        move_attributes = requests.get(request_move).json()
        if move_attributes["generation"]["name"] == "generation-i":
            moves_dict[next_move["name"]]["power"] = move_attributes["power"]
            moves_dict[next_move["name"]]["accuracy"] = move_attributes["accuracy"]
            moves_dict[next_move["name"]]["type"] = move_attributes["type"]["name"]
            moves_dict[next_move["name"]]["pp"] = move_attributes["pp"]

    with open(json_path, "w") as json_file:
        json.dump(moves_dict, json_file)


if __name__ == "__main__" :
    #get_pokemon("pokemon.json")
    #get_types("pokemon_types.json")
    #get_moves("pokemon_moves.json")