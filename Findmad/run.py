from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
from classes import Users, Recipe
from forms import LoginForm, RegisterForm, RecipeForm
import bcrypt
import psycopg2

# Initialize the flask app:)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://recipe:recipe@localhost:5433/recipe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Initialize Flask-Login for user session management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' ## If a user is not logged in they ar redirected to the login view

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))   # SELECT * FROM users WHERE id = id

#Route for Home
@app.route('/')
def home():
    return render_template('home.html')  # Render the home template

#Route for Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password) #Create a new user instance
        db.session.add(new_user) # Add the new user to the database
        db.session.commit() # commit, so they are actually added
        # SQL: INSERT INTO users (username, email, password) VALUES (form.username.data, form.email.data, hashed_password)
        flash(f'Account created for {form.username.data}!', 'success') # if it works flash this message
        return redirect(url_for('home')) # Then redirect home
    return render_template('register.html', form=form)  #If the form submission is not valid they are directed to register.

#Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        # SQL: SELECT * FROM users WHERE username = form.username.data LIMIT 1
        if user and check_password_hash(user.password, form.password.data): #checks if the user exists and if it matches the password
            login_user(user) #logs the user in
            flash(f'Logged in as {form.username.data}', 'success') # show succes message
            return redirect(url_for('home')) #Direct the user to the homepage
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger') # show login unsuccesful message
    return render_template('login.html', form=form) #If the form submission is not valid, the user is directed to login a(gain)


#Route for Adding a Recipe
@app.route('/recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        new_recipe = Recipe(name=form.name.data, steps=form.steps.data, ingredients=form.ingredients.data, 
            n_steps=form.n_steps.data, n_ingredients=form.n_ingredients.data)  #Create a new recipe instance
        db.session.add(new_recipe) #add the recipe to the database
        db.session.commit() #commit, so it is actually added to the database
        #SQL: INSERT INTO recipes (name, steps, ingredients, n_steps, n_ingredients) VALUES (form.name.data, form.steps.data, form.ingredients.data, form.n_steps.data, form.n_ingredients.data)
        flash(f'Recipe {form.name.data} added!', 'success') #flash succes, as it worked
        return redirect(url_for('home')) # then the user is directed home again
    return render_template('recipe.html', form=form)  #if the submission didnt work, render the recipe template.

#Route for viewing recipies
@app.route('/recipes', methods=['GET'])
@login_required
def view_recipes():
    recipes = Recipe.query.with_entities(Recipe.id, Recipe.name).all() # select all recipes and get their IDs and names
    #SQL: SELECT id, name FROM recipes
    return render_template('view_recipes.html', recipes=recipes) #render the view-recipes template

#Route for viewing a specific recipe
@app.route('/recipe/<int:recipe_id>', methods=['GET'])
@login_required
def view_recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id) # get the recipe
    #SQL: SELECT * FROM recipes WHERE id = recipe_id
    return render_template('recipe_detail.html', recipe=recipe) #view "that" recipe

#Route for search recipies by ingredients
@app.route('/search', methods=['GET'])
@login_required
def search_recipes():
    ingredient = request.args.get('ingredient')
    if ingredient:
        recipes = Recipe.query.filter(Recipe.ingredients.ilike(f'%{ingredient}%')).all() #find recipies that contain the ingredient
        #SQL SELECT * FROM recipes WHERE ingredients ILIKE '%ingredient%'
        return render_template('search_results.html', recipes=recipes, ingredient=ingredient) #Render the search_results-template with the search results based on your search
    else:
        return redirect(url_for('home')) #redirect to homepage(if no ingredient is provided in the search)


#Route for login out
@app.route('/logout')
def logout():
    logout_user() #log the user out
    return redirect(url_for('home')) #redirect the user to the home page(CHANGE TO LOGIN PAGE)


# Run the Flask APP
if __name__ == '__main__':
    app.run(debug=True)
