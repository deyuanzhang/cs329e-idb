import json

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def get_gen1_move():
    move = load_json('pokemon_moves.json')
    gen1_moves = [] 
    for next_move in move:
        gen1_moves.append(next_move)
    return gen1_moves

gen1_moves = get_gen1_move()
		