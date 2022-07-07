from flask_app.models.magazine import Magazine
from flask import render_template, redirect, request, session
from flask_app import app
from flask import flash
from flask_app.models.user import User

##display route##
@app.route("/magazines/new")
def display_magazine_form():
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")

    data = {
        "id" : session['id']
    }

    user_in_db = User.get_one_user(data)

    User.get_one_user(data)

    return render_template("/magazine_form.html", user_in_db = user_in_db)

@app.route("/magazines/<int:id>")
def display_one_magazine(id):
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")

    one_magazine = {
        "id" : id,
    }

    data = {
        "id" : session['id']
    }

    user_in_db = User.get_one_user(data)

    one_magazine = Magazine.get_one_magazine(one_magazine)
    return render_template("magazine_information.html", one_magazine = one_magazine, user_in_db = user_in_db)



## create route ##
@app.route("/magazines/add_magazine", methods=['POST'])
def add_magazine():
    if not session:
        flash("You are not logged in! Please login to continue", 'login')
        return redirect("/")
    
    errors = False

    if len(request.form['name']) < 3:
        flash("Name must be at least 3 characters!", 'name_length')
        errors = True
    
    if len(request.form['description']) < 10:
        flash("Description must be at least 10 characters!", 'description_length')
        errors = True


    if errors:
        return redirect("/magazines/new")

    new_magazine = {
    "name" : request.form['name'],
    "description" : request.form['description'],
    "user_id" : session['id']
    }

    Magazine.add_magazine(new_magazine)
    return redirect("/dashboard")

##delete route ##
@app.route("/magazines/<int:id>/delete")
def delete_magazine(id):
    one_magazine = {
        'id' : id
    }

    data = {
        "id" : session['id']
    }

    User.get_one_user(data)

    Magazine.delete_one_magazine(one_magazine)

    return redirect(f"/user/{id}/update_user")
