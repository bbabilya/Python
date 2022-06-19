from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo


#######DISPLAY ROUTES########
@app.route("/")
def redirecting_user():
    return redirect("/dojos")

@app.route("/dojos")
def show_all_dojos():
    all_dojos = Dojo.get_all_dojos()
    #the class method is already providing our information for us, so we just need to call the function from Dojo model.

    return render_template("index.html", all_dojos = all_dojos)
    #returning view of index.html, and calling the variable to display all dojos.


######CREATE ROUTES#######
@app.route("/add_new_dojo", methods = ['POST'])
def add_one_dojo():
    newDojo = {
        'name' : request.form['name']
    }
    Dojo.add_one_dojo(newDojo)
    return redirect("/")
