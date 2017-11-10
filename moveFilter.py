import json

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

#get all the moves present in generation 1 only 
#api scraper limits to 300 a day, runs out quickly
def get_gen1_move():
    move = load_json('pokemon_moves.json')
    gen1_moves = [] 
    for next_move in move:
        gen1_moves.append(next_move)
    return gen1_moves

gen1_moves = get_gen1_move()
		