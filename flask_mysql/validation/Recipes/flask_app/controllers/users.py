from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import render_template, redirect, request, session
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


###DISPLAY ROUTES###
@app.route("/")
def display_main():
    return render_template("index.html")

@app.route("/dashboard")
def display_dashboard():
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")

    data = {
        "id" : session['id']
    }

    user_in_db = User.get_one_user(data)
    all_recipes = Recipe.get_all_recipes()

    return render_template("dashboard.html", user_in_db = user_in_db, all_recipes = all_recipes)

###LOG OUT###
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

###CREATE ROUTES###
@app.route("/create/user", methods=['POST'])
def create_new_user():
    password_hash = bcrypt.generate_password_hash(request.form['password'])

    SpecialSym =['$', '@', '#', '%', '-']

    #validations for password, email, first_name and last_name requirements
    errors = False

    if len(request.form['first_name']) < 2:
        flash("First Name must be at least 2 characters!", 'first_name_length')
        errors = True

    if len(request.form['last_name']) < 2:
        flash("Last Name must be at least 2 characters!", 'last_name_length')
        errors = True

    if not request.form['password'] == request.form['confirm_password']:
        flash("Passwords do not match, please try again!", 'password_matching')
        errors = True
    
    if len(request.form['password']) < 8:
        flash("Password must be 8 characters or longer!", 'password_error')
        errors = True
    
    if not any(char in SpecialSym for char in request.form['password']):
        flash("Password must contain a special character!", 'password_error')
        errors = True
    
    if not any(char.isdigit() for char in request.form['password']):
        flash("Password must contain a number!", 'password_error')
        errors = True

    if not User.validate_user(request.form):
        errors = True

    if errors:
        return redirect("/")

    new_user = {
    "first_name" : request.form['first_name'],
    "last_name" : request.form['last_name'],
    "email" : request.form['email'],
    "password" : password_hash
    }
    #"password" takes in the variable password_hash above that takes request.form['password'] and transforms it into a hash

    id = User.add_user(new_user)
    session['id'] = id
    return redirect("/dashboard")


@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.unique_email(data)

    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect("/")


    session['id'] = user_in_db.id

    return redirect("/dashboard")