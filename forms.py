from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length

class TrainerAddForm(FlaskForm):
    """Registration form for new trainer."""

    trainer_name = StringField("Trainer Name")
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)]) 
    image_url = FileField('(Optional) Image URL', validators=[FileAllowed(['jpg', 'png', 'jfif', 'jpeg'], 'Images only!')])

class LoginForm(FlaskForm):
    """Login form for validated trainer."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
