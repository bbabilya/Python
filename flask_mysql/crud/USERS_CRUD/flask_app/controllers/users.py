from flask_app.models.user import User
#importing the user class in our controllers
from flask import render_template, redirect, request
#uses import of render_template, redirect, request, session, etc
from flask_app import app 
#uses approute


#########DISPLAY ROUTES#########
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users_list = User.get_all()
    return render_template("index.html", users_list = users_list)

@app.route("/user/<int:id>")
def display_one_user(id):
    data = {
        'id' : id
    }
    one_user = User.get_one_user(data)
    return render_template("displayuser.html", one_user = one_user)

@app.route("/create")
def create_page():
    return render_template("create.html")


@app.route("/user/<int:id>/edit_form")
def display_edit_user(id):
    one_user = {
        'id' : id
    }
    one_user = User.get_one_user(one_user)
    return render_template("edituser.html", one_user = one_user)



#########CREATE ROUTES#########
@app.route("/create/user", methods = ['POST'] )
def create_user():
    newUser = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form["email"]
    }
    newUser_id = User.create_user(newUser)
    return redirect(f"/user/{newUser_id}")


@app.route("/user/<int:id>/update", methods=['POST'])
def edit_one_user(id):
    newUser = {
        'id' : id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form["email"]
    }
    User.edit_one_user(newUser)
    return redirect(f"/user/{newUser['id']}")



####### DELETE ROUTES #######
@app.route("/user/<int:id>/delete")
def delete_user(id):
    deleteUser = {
        'id' : id
    }
    User.delete_one_user(deleteUser)
    return redirect("/")