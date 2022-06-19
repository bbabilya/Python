from flask import Flask, render_template, request, redirect
# import the class from user.py
from users import User
app = Flask(__name__)


# MAIN ROUTE, SHOWS ALL USERS
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users_list = User.get_all()
    return render_template("index.html", users_list = users_list)


# RENDER TEMPLATE FOR CREATE USER
@app.route("/create")
def create_page():
    return render_template("create.html")


# CREATE USER
@app.route("/create/user", methods = ['POST'] )
def create_user():
    newUser = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form["email"]
    }
    User.create_user(newUser)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)