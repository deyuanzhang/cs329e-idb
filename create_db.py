import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment 
from models import engine
from models import Base
from models import Pokemon
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

		
create_pokemon()
