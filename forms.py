from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, EqualTo, ValidationError

from models import Trainer

class TrainerAddForm(FlaskForm):
    """Registration form for new trainer."""

    trainer_name = StringField("Trainer Name", validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm_password', message="Passwords must match!")]) 
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])
    image_url = FileField('(Optional) Image URL', validators=[FileAllowed(['jpg', 'png', 'jfif', 'jpeg'], 'Images only!')])

    def validate_username(self, username):
        user = Trainer.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already taken!")

    def validate_trainer_name(self, trainer_name):
        trainer = Trainer.query.filter_by(trainer_name=trainer_name.data).first()
        if trainer:
            raise ValidationError("Trainer Name already taken!")

class LoginForm(FlaskForm):
    """Login form for validated trainer."""

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm_password', message="Passwords must match!")]) 
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])
