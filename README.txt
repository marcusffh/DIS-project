MADE BY
Noah Wenneberg Junge - qxk266 - zqw671@alumni.ku.dk
And
Marcus Frehr Friis-Hansen - lns611 - lns611@alumni.ku.dk

Group 30




STEPS TO INITIALIZE THE DATABASE
1. Star by opening an psql interactive session:
    psql -U postgres -d postgres -h localhost -p 5433


2. Create database called recipe with port 5433
    CREATE DATABASE recipe;
    CREATE USER recipe WITH PASSWORD 'recipe';


3. CHANGE TO RECIPE DATABASE AS SUPERUSER "POSTGRES"
    with: from the postgres database
        \c recipe
    or
        psql -U postgres -d recipe -h localhost -p 5433


4. create user recipe priviligesd, remember to do it as a superuser in the recipe database
    GRANT ALL PRIVILEGES ON DATABASE recipe TO recipe;
    GRANT ALL PRIVILEGES ON SCHEMA public TO recipe;
    GRANT CREATE ON SCHEMA public TO recipe;


5. GO TO Findmad directory TERMINAL and install requirements.txt
    pip install -r requirements.txt


6. Copy path from create_tables.sql in vscode and upload create_tables.sql to database 
        psql -U recipe -d recipe -h localhost -p 5433 -f /pathto/create_tables.sql
    Example:
        psql -U recipe -d recipe -h localhost -p 5433 -f /Users/marcusfriis-hansen/Desktop/Uni/Databases_and_Information_Systems/project/DIS-project/Findmad/create_tables.sql


7. open a psgl interactive shell in recipe database as recipe user
    psql -U recipe -d recipe -h localhost -p 5433


8.upload data to database
        \copy recipe(name,n_steps,steps,description,ingredients,n_ingredients) FROM /path_to/DATA.csv DELIMITER ',' CSV HEADER;
    Example:
        \copy recipe(name,n_steps,steps,description,ingredients,n_ingredients) FROM /Users/marcusfriis-hansen/Desktop/Uni/Databases_and_Information_Systems/project/DIS-project/Findmad/DATA.csv DELIMITER ',' CSV HEADER;


9. run the app from the "findmad folder" 
    python run.py

10. copy the link and paste it into a browsers


IF SOMETHING WENT WRONG AND YOU WANT TO START OVER:
1. Start by opening an psql interactive session:
    psql -U postgres -d postgres -h localhost -p 5433


2. remove any old attempts at getting this to work
    DROP DATABASE IF EXISTS recipe;

3.  remove old user in former attempts
    REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM recipe;
    REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM recipe;
    REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM recipe;
    DROP OWNED BY recipe;
    DROP ROLE recipe;




WHAT FEATURES DOES THE WEBSITE HAVE

    REGISTER
    here you can register an account with username, mail and password. We use regex to make sure we	only accept “real“ mails
    and other regex to make sure passwords consist of both letters and numbers

    LOGIN
    login with the username and password registered earlier to access the features of our site

    HOMEPAGE
    When logged in you get a good overview of the entire web-apps functionality, including our actual 	features.

    SEARCH RECIPIES
    From here you can search through recipes by stating an ingredient

    ADD RECIPIES
    You are also given the option of adding your very own recipes to the database

