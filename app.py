from flask import Flask, render_template, redirect, flash, session, g
from models import db, connect_db, Trainer, Pokemon, Move, PokemonType, Location
from forms import LoginForm, TrainerAddForm
from werkzeug.utils import secure_filename

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

import requests
import random
import os

uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretpokemon@app"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(uri, 'postgresql:///cichorium')
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
app.config['DEBUG'] = False




app.app_context().push()

connect_db(app)
db.create_all()

#####################
# GLOBAL VARIABLES
#####################

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"
GENERATION_URL = "https://pokeapi.co/api/v2/generation/"

CURRENT_TRAINER = "current_trainer"

TYPE_COLORS = {
	'normal': '#A8A77A',
	'fire': '#EE8130',
	'water': '#6390F0',
	'electric': '#F7D02C',
	'grass': '#7AC74C',
	'ice': '#96D9D6',
	'fighting': '#C22E28',
	'poison': '#A33EA1',
	'ground': '#E2BF65',
	'flying': '#A98FF3',
	'psychic': '#F95587',
	'bug': '#A6B91A',
	'rock': '#B6A136',
	'ghost': '#735797',
	'dragon': '#6F35FC',
	'dark': '#705746',
	'steel': '#B7B7CE',
	'fairy': '#D685AD',
}


#####################
# TRAINER / LOGIN ROUTES 
#####################

@app.before_request
def add_trainer_to_global():

    if CURRENT_TRAINER in session:
        g.trainer = Trainer.query.get(session[CURRENT_TRAINER])

    else:
        g.trainer = None
    
def login_trainer(trainer):
    """Auto login the trainer."""

    session[CURRENT_TRAINER] = trainer.id

def logout_trainer():
    """Logout trainer."""

    if CURRENT_TRAINER in session:
        del session[CURRENT_TRAINER]

@app.errorhandler(404)
def invalid_route(e):
    """
    If user accesses a non-existant route.
    Redirect user to the /pokemon route.
    """

    return redirect('/pokemon')

def upload_to_static_folder(file_storage):
    """ Extract the filename and store in static working directory."""

    static_dir = os.path.join(os.path.dirname(app.instance_path), 'static')
    filename = secure_filename(file_storage.filename)
    file_storage.save(os.path.join(static_dir, filename))

    return filename

@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    """Handles signing up new trainers."""

    # Make sure enctype="multipart/form-data" is added in the POST form html file.
    form = TrainerAddForm()

    if form.validate_on_submit():

        trainer_name = form.trainer_name.data
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        img_url = form.image_url.data or Trainer.image_url.default.arg

        trainer = Trainer(
                            trainer_name=trainer_name,
                            username=username,
                            password=password,
                            image_url=upload_to_static_folder(img_url)
                        )
                    
        db.session.add(trainer)
        db.session.commit()

        session[CURRENT_TRAINER] = trainer.id

        return redirect('/pokemon')
    
    else:
        return render_template('/users/new_user.html', form=form)

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    """Show login form and validate."""

    if CURRENT_TRAINER in session:
        return redirect('/pokemon')

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        trainer = Trainer.authenticate(username, password)

        if trainer:
            session[CURRENT_TRAINER] = trainer.id
            return redirect('/pokemon')
    
    return render_template('/users/login_user.html', form=form)


@app.route('/users/logout')
def logout():
    """Route to log out trainer."""

    logout_trainer()
    return redirect('/pokemon')

#####################
# GLOBAL FUNCTIONS
#####################

def add_pokemon_locations(pokemon_loc_response, pokemon_id):
    """
    Add all locations of a pokemon to the database.
    Assign the location name to an increment location ID
    Assign the same pokemon id to all locations.
    """
    for location_object in pokemon_loc_response:
        new_location = Location(name = location_object['location_area']['name'], pokemon_id = pokemon_id)
        db.session.add(new_location)
    
def add_pokemon_types(pokemon_types, pokemon_id):
    """
    Add all types of a pokemon to the database.
    Assign the type name to an increment type ID
    Assign the same pokemon id to all types.
    """

    for type in pokemon_types:
        new_type = PokemonType(name = type['type']['name'], pokemon_id = pokemon_id)
        db.session.add(new_type)

def return_pokemon_weaknesses(type_name):
    """
    Send a request to the pokemon type API using the type name.
    Go through the JSON to retrieve the damage relations dict
    Extract all the type name and create an array of weakness types.
    Return the array.
    """

    type_object = requests.get("https://pokeapi.co/api/v2/" + f"type/{type_name}").json()
    damage_relations_object = type_object['damage_relations']

    double_damage = []
    for name in damage_relations_object['double_damage_from']:
        double_damage.append(name['name'])

    return double_damage

def add_pokemon_moves(pokemon_moves, pokemon_id):
    """
    Add all 5 moves available to the pokemon to the database.
    Assign the move name to an increment move ID
    Assign the same pokemon id to all moves.
    """

    counter = 1
    moveset = {}

    for move in pokemon_moves:
        counter = counter + 1
        moveset[counter] = move['move']['name']

    for i in range (5):
        random_number = random.randint(0, counter)
        if random_number in moveset.keys():
            new_move = Move(name = moveset.pop(random_number), pokemon_id = pokemon_id)
            db.session.add(new_move)
        else:
            random_number = random.randint(1, counter)

#####################
# POKEMON ROUTES
#####################

@app.route('/')
def redirect_to_pokemon():
    """Redirect to /pokemon route."""

    return redirect('/pokemon')

@app.route('/pokemon')
def show_home():
    """Display home page"""

    if not CURRENT_TRAINER in session:
        return render_template('homepage.html')

    else:
        trainer = Trainer.query.get_or_404(g.trainer.id)

        return render_template('homepage.html', trainer=trainer)

@app.route('/pokemon/list')
def list_all_pokemon():
    """
    List all of the pokemons from each generation.
    This route uses JavaScript app.js to dynamically 
    retrieve and update the page.
    """

    return render_template('/pokemon/pokemon_list.html')

@app.route('/pokemon/add_or_info/<int:id>/<method>', methods=['GET', 'POST'])
def add_or_show_pokemon(id, method):
    """
    Handles showing pokemon information if method is GET.
    Handles adding pokemon to the trainer's team if method is POST.
    """

    pokemons = {}
    pokemon_types = []
    merged_weakness_list = []


    pokemon_response = requests.get(POKEMON_URL + str(id)).json()
    pokemon_loc_response = requests.get(POKEMON_URL + str(id) + "/encounters").json()
    
    p_moveset = pokemon_response['moves']
    p_name = pokemon_response['name']
    p_stats = pokemon_response['stats']
    
    p_id = pokemon_response['id']
    pokemons[p_id] = p_name.upper()

    p_types = pokemon_response['types']
    for type in p_types:
        pokemon_types.append(type['type']['name'])
        weakness_list = return_pokemon_weaknesses(type['type']['name'])    
        merged_weakness_list = merged_weakness_list + weakness_list

    merged_weakness_list = list(dict.fromkeys(merged_weakness_list))

    if method == "post":
        if not CURRENT_TRAINER in session:
            flash("No team to add pokemons in.")
            flash("Create an account or login!")
            return redirect('/pokemon/list')
        
        trainer_id = Trainer.query.get_or_404(g.trainer.id)

        add_pokemon_to_trainer = Pokemon(name = pokemon_response['name'], trainer_id=trainer_id.id, image_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png")
        db.session.add(add_pokemon_to_trainer)
        db.session.commit()

        add_pokemon_locations(pokemon_loc_response, add_pokemon_to_trainer.id)
        add_pokemon_types(pokemon_response['types'], add_pokemon_to_trainer.id)
        add_pokemon_moves(pokemon_response['moves'], add_pokemon_to_trainer.id)

        db.session.commit()

        flash(f"{pokemon_response['name'].upper()} has been captured!")
        return redirect('/pokemon')

    else:
        return render_template('/pokemon/pokemon_info.html', 
                                    p_id=p_id,
                                    pokemons=pokemons, 
                                    p_moveset=p_moveset,
                                    p_stats=p_stats,
                                    pokemon_loc_response=pokemon_loc_response,
                                    pokemon_types=pokemon_types,
                                    weakness_list=merged_weakness_list,
                                    pokemon_type_colors=TYPE_COLORS)

@app.route('/pokemon/delete/<int:id>')
def remove_pokemon_from_trainer(id):
    """ Trainer will remove a pokemon from their team. """

    pokemon = Pokemon.query.get_or_404(id)

    flash(f"{pokemon.name.upper()} has been released in the wild!")

    db.session.delete(pokemon)
    db.session.commit()

    return redirect('/pokemon')
