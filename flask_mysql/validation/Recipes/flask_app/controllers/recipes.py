from flask_app.models.recipe import Recipe
from flask import render_template, redirect, request, session
from flask_app import app
from flask import flash
from flask_app.models.user import User

###DISPLAY ROUTES###
@app.route("/recipes/new")
def display_recipe_form():
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")

    return render_template("/recipe_form.html")

@app.route("/recipes/<int:id>/edit")
def display_edit_form(id):
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")

    one_recipe = {
        'id' : id
    }

    one_recipe = Recipe.get_one_recipe(one_recipe)
    return render_template("/edit_recipe.html", one_recipe = one_recipe)

@app.route("/recipes/<int:id>")
def display_recipe(id):
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")

    one_recipe = {
    'id' : id
    }

    data = {
    "id" : session['id']
    }

    user_in_db = User.get_one_user(data)
    one_recipe = Recipe.get_one_recipe(one_recipe)
    return render_template("recipe.html", one_recipe = one_recipe, user_in_db = user_in_db)


###CREATE ROUTES###
@app.route("/recipes/add_recipe", methods=['POST'])
def add_recipe():
    errors = False

    if len(request.form['name']) < 3:
        flash("Name must be at least 3 characters!", 'name_length')
        errors = True
    
    if len(request.form['description']) < 3:
        flash("Description must be at least 3 characters!", 'description_length')
        errors = True
    
    if len(request.form['instructions']) < 3:
        flash("Instructions must be at least 3 characters!", 'instructions_length')
        errors = True
    
    if len(request.form['date_made']) < 1:
        flash("Please submit a Date", 'date_made_length')
        errors = True

    if 'cooking_time' not in request.form:
        flash("Please pick an Option", 'cooking_time_length')
        errors = True

    if 'date_made' not in request.form:
        flash("Please pick an option", 'date_made_length')

    if errors:
        return redirect("/recipes/new")

    new_recipe = {
    "name" : request.form['name'],
    "description" : request.form['description'],
    "instructions" : request.form['instructions'],
    "date_made" : request.form['date_made'],
    "cooking_time" : request.form['cooking_time'],
    "user_id" : session['id']
    }

    Recipe.add_recipe(new_recipe)
    return redirect("/dashboard")

@app.route("/recipes/<int:id>/update", methods=['POST'])
def edit_recipe(id):
    errors = False

    if len(request.form['name']) < 3:
        flash("Name must be at least 3 characters!", 'name_length')
        errors = True
    
    if len(request.form['description']) < 3:
        flash("Description must be at least 3 characters!", 'description_length')
        errors = True
    
    if len(request.form['instructions']) < 3:
        flash("Instructions must be at least 3 characters!", 'instructions_length')
        errors = True
    
    if len(request.form['date_made']) < 1:
        flash("Please submit a Date", 'date_made_length')
        errors = True

    if 'cooking_time' not in request.form:
        flash("Please pick an Option", 'cooking_time_length')
        errors = True

    if 'date_made' not in request.form:
        flash("Please pick an option", 'date_made_length')

    if errors:
        return redirect(f"/recipes/{id}/edit")

    new_recipe = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date_made" : request.form['date_made'],
        "cooking_time" : request.form['cooking_time'],
        'id' : id
    }

    Recipe.edit_recipe(new_recipe)
    return redirect(f"/recipes/{new_recipe['id']}")


###DELETE ROUTES###
@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    one_recipe = {
        'id' : id
    }

    Recipe.delete_one_recipe(one_recipe)

    return redirect("/dashboard")