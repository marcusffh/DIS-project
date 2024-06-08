from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp

#form for login, defines what informations is required for a login and the scope of the characters in username and password
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) 
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login') 

#Form for adding recipes
class RecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=1000)])
    steps = StringField('Steps', validators=[DataRequired(), Length(max=100)])
    ingredients = StringField('Ingredients', validators=[DataRequired(), Length(max=100)])
    n_steps = FloatField('Number of steps', validators=[DataRequired()])
    n_ingredients = FloatField('Number of ingredients', validators=[DataRequired()])
    submit = SubmitField('Add Recipe')

#Form for registering users, notice the criteria.
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[
        DataRequired(),
        Regexp(r'^[\w\.-]+@[\w\.-]+\.\w+$', message="Invalid email address.")# we use Regex to make sure the user enters a "valid" email
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Regexp(r'[a-zA-Z]+\d+|\d+[a-zA-Z]+', message="Password must contain at least one number and letter.") # We use regex to make sure the password contains at least one letter ane one number, to somewhat aid in security
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')



##Fields are the "input-forms" that lets users input data, the forms also desribe the criteria for filling them out