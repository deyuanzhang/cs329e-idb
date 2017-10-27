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
from flask import render_template # Import render_template function

app = Flask(__name__)


@app.route('/')  # URL for function (default for home page)
@app.route('/index')  # Secondary URL for function
def index():
    return render_template('home.html')  # located in templates/

@app.route('/pokemon')  
def pokemon():
    return render_template('pokemonSplash.html') 

@app.route('/types')  
def types():
    return render_template('typesSplash.html') 

@app.route('/moves')  
def moves():
    return render_template('movesSplash.html') 

@app.route('/bio')  
def bio():
    return render_template('about.html') 

@app.route('/bulbasaur')  
def bulbasaur():
    return render_template('bulbasaur.html') 

@app.route('/charmander')  
def charmander():
    return render_template('charmander.html') 

@app.route('/fire')  
def fire():
    return render_template('fire.html') 

@app.route('/grass')  
def grass():
    return render_template('grass.html') 

@app.route('/hydropump')  
def hydropump():
    return render_template('hydropump.html') 

@app.route('/inferno')  
def inferno():
    return render_template('inferno.html') 

@app.route('/seedbomb')  
def seedbomb():
    return render_template('seedbomb.html') 

@app.route('/squirtle')  
def squirtle():
    return render_template('squirtle.html') 

@app.route('/water')  
def water():
    return render_template('water.html') 

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
