from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database import db
import bcrypt

# The recipe table
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #primary key for the table
    name = db.Column(db.String(1000), nullable=False)
    n_steps = db.Column(db.String(1000), nullable=False)
    steps = db.Column(db.String(1000), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    n_ingredients = db.Column(db.Float)

    #This method returns a string representing an instance of the recipe table
    def __repr__(self):
        return f'<Recipe {self.name}>'


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #primary key for the table
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    # This method returns a string representing the user ID
    def get_id(self):
        return str(self.id)

    #This method returns a string representing an instance of the Users-table
    def __repr__(self):
        return f'<User {self.username}>'