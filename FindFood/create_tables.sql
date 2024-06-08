-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS favorite_recipes, recipes, users;

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create favorite_recipes table
CREATE TABLE favorite_recipes (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    recipe_name VARCHAR(255),
    recipe_details TEXT
);

-- Create recipes table with appropriate data types
CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    n_steps INTEGER,
    steps TEXT,
    description TEXT,
    ingredients TEXT,
    n_ingredients INTEGER
);

-- Create some initial users for testing
INSERT INTO users (username, email, password) VALUES ('testuser', 'testuser@example.com', 'testpassword');
