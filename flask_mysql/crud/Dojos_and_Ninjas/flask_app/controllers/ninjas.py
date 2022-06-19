from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#####DISPLAY ROUTES########
@app.route("/<int:dojo_id>")
def show_one_dojo(dojo_id):
    data = {
        'dojo_id' : dojo_id
    }
    one_dojo = Ninja.show_one_dojo(data)

    return render_template("show_dojo.html", one_dojo = one_dojo)

@app.route("/add_ninja_form")
def display_ninja_form():
    all_dojos = Dojo.get_all_dojos()
    return render_template("add_ninja.html", all_dojos = all_dojos )



#####CREATE ROUTES########
@app.route("/add_ninja", methods = ['POST'])
def add_a_ninja():
    newNinja = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    Ninja.add_one_ninja(newNinja)
    return redirect(f"/{newNinja['dojo_id']}")


