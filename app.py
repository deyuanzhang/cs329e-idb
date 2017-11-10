# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask
from flask import render_template, request, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pokemon, Type, Move, engine
from moveFilter import gen1_moves
from create_db import create_pokemon, session


app = Flask(__name__)


@app.route('/')  # URL for function (default for home page)
@app.route('/index')  # Secondary URL for function
def index():
    return render_template('home.html')  # located in templates/

@app.route('/pokemon', defaults ={'pokemon_name':None})
@app.route('/pokemon/<pokemon_name>')
def pokemon(pokemon_name):
    if pokemon_name == None:
        pokemon_all = session.query(Pokemon).all()
        return render_template('pokemonSplash.html', pokemon_all = pokemon_all)
    else:
        pokemon_samp = session.query(Pokemon).filter_by(name = pokemon_name)
        types = pokemon_samp[0].type[1:-1].split(',')
        temp_moves = pokemon_samp[0].move[1:-1].split(',')
        moves = []
        for m in temp_moves:
            if m in gen1_moves:
                moves.append(m)
        attack = pokemon_samp[0].attack
        defense = pokemon_samp[0].defense
        spattack = pokemon_samp[0].specialattack
        spdefense = pokemon_samp[0].spdefense
        return render_template('pokemonTemplate.html', pokemon=pokemon_samp[0], types = types, moves=moves, attack=attack, defense=defense, spattack=spattack, spdefense=spdefense)  # located in templates/

@app.route('/types', defaults ={'type_name':None})
@app.route('/types/<type_name>')
def types(type_name):
    if type_name == None:
        type_all = session.query(Type).all()
        return render_template('typesSplash.html', type_all = type_all)
    else:
        type_samp = session.query(Type).filter_by(name = type_name)
        half_to = type_samp[0].half_to[1:-1].split(',')
        half_from = type_samp[0].half_from[1:-1].split(',')
        double_to = type_samp[0].double_to[1:-1].split(',')
        double_from = type_samp[0].double_from[1:-1].split(',')
        return render_template('typeTemplate.html', type=type_samp[0], half_to=half_to, half_from = half_from, double_to = double_to, double_from = double_from)  # located in templates/

@app.route('/moves', defaults ={'move_name':None})
@app.route('/moves/<move_name>')
def moves(move_name):
    if move_name == None:
        move_all = session.query(Move).all()
        return render_template('movesSplash.html', move_all = move_all)
    else:
        move_samp = session.query(Move).filter_by(name = move_name)
        power = move_samp[0].power
        accuracy = move_samp[0].accuracy
        type = move_samp[0].type
        pp = move_samp[0].pp
        return render_template('moveTemplate.html', move=move_samp[0], type=type, accuracy=accuracy, pp=pp, power=power)  # located in templates/


@app.route('/bio')
def bio():
    return render_template('about.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
