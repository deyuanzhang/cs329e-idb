import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment 
from models import engine
from models import Base
from models import Pokemon
from models import Move
from models import Type
from moveFilter import gen1_moves
from sqlalchemy.orm import sessionmaker

# bind the engine to the base class. This makes the connection
# between our class definitions and the corresponding tables 
# within our database
Base.metadata.bind = engine

# create session maker object to establish a link 
# of communication between our code execution and 
# the engine we just created
DBSession = sessionmaker(bind=engine)

# in order to create, read, update or delete information 
# on our database, SQLAlchmey executes database operations
# via an interface called a session.
# A session allows us to write down all the commands 
# we want to execute but not send them to the DB 
# until we call "commit"
# create an instance of DBSession
session = DBSession()

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_pokemon():
    pokemon = load_json('pokemon.json')

    for next_pokemon in pokemon:
        print("working pokemon" + next_pokemon)
        name = next_pokemon
        type = pokemon[next_pokemon]['type']
        move = pokemon[next_pokemon]['moves']
        attack = pokemon[next_pokemon]['attack']
        defense = pokemon[next_pokemon]['defense']
        spdefense = pokemon[next_pokemon]['special-defense']
        specialattack = pokemon[next_pokemon]['special-attack']
        image = pokemon[next_pokemon]['img']
        
		
        newPokemon = Pokemon(name = name, type = type, move = move, attack = attack, defense = defense, spdefense = spdefense, specialattack = specialattack, image = image)
		# After I create the book, I can then add it to my session. 
        session.add(newPokemon)
		# commit the session to my DB.
        session.commit()
        
def create_move():
    move = load_json('pokemon_moves.json')

    for next_move in move:
        print(next_move)
        name = next_move
        power = move[next_move]['power']
        accuracy = move[next_move]['accuracy']
        type = move[next_move]['type']
        pp = move[next_move]['pp']
		
        newMove = Move(name = name, power = power, accuracy = accuracy, type = type, pp = pp)
        # After I create the book, I can then add it to my session. 
        session.add(newMove)
	# commit the session to my DB.
        session.commit()
        
def create_type():
    type = load_json('pokemon_types.json')

    for next_type in type:
        print(next_type)
        name = next_type
        half_to = type[next_type]['half_to']
        half_from = type[next_type]['half_from']
        double_to = type[next_type]['double_to']
        double_from = type[next_type]['double_from']
		
        newType = Type(name = name, half_to = half_to, half_from = half_from, double_to = double_to, double_from = double_from)
        # After I create the book, I can then add it to my session. 
        session.add(newType)
	# commit the session to my DB.
        session.commit()



create_pokemon()	
create_move()
create_type()
