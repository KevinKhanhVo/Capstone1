from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

db = SQLAlchemy()

class Trainer(db.Model):
    """Trainer table."""

    __tablename__ = "trainer"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trainer_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text,default="no-pic-default.jpg")

    pokemon = db.relationship('Pokemon', cascade="all, delete")

    """Method to authenticate valid users."""
    @classmethod
    def authenticate(cls, username, pwd):
        trainer = Trainer.query.filter_by(username=username).first()

        if trainer and bcrypt.check_password_hash(trainer.password, pwd):
            return trainer
        else:
            return False

class Pokemon(db.Model):
    """Pokemon table."""

    __tablename__ = "pokemon"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    trainer_id = db.Column(db.Integer, ForeignKey("trainer.id"))
    image_url = db.Column(db.Text)

    moves = db.relationship('Move', cascade="all, delete")
    types = db.relationship('PokemonType', cascade="all, delete")
    location = db.relationship('Location', cascade="all, delete")

class Move(db.Model):
    """Move table."""

    __tablename__ = "move"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    pokemon_id = db.Column(db.Integer, ForeignKey("pokemon.id"))

class PokemonType(db.Model):
    """Pokemon Type table."""

    __tablename__ = "pokemontype"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    pokemon_id = db.Column(db.Integer, ForeignKey("pokemon.id"))

class Location(db.Model):
    """Location table."""

    __tablename__ = "location"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    pokemon_id = db.Column(db.Integer, ForeignKey("pokemon.id"))

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

