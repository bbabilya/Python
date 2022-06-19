from flask import Flask, render_template, request, redirect, session

#importing Flask, Flask is now a class.
#render_template is a function for calling the html template
#request -- grabs from html, redirect -- business logic, are for the action route. They come from flask.

app = Flask(__name__)
#application launch!
app.secret_key = "secret"
#secret key for session integration

#list of dictionaries for to-do list.
list_todos = [{
    "todo" : "Learn Templates in Flask",
    "status" : "In Progress"
},
{
    "todo" : "Learn Object Oriented Programming",
    "status" : "Complete"
},
{
    "todo" : "Learn Deployment",
    "status" : "Cancelled"
}]


#display routes - display something on a screen
@app.route("/alfredo")
#this defines your route url. You have to go to this address to show any content.

@app.route ("/") #Mainpage!
@app.route("/todos")
def get_all_todos():
    # if "num_of_visits" in session:
    #     session["num_of_visits"] += 1
    # else:
    #     session["num_of_visits"] = 1

    return render_template("index.html", first_name = "Alexander", list_todos = list_todos) 
#connecting html template to our back-end.
#Alexander becomes a variable that can be referred to in HTML.

"""
Restful applications allow us to update something, delete something, create something.
"""
@app.route("/todo/new")
def display_create_todo():
    return render_template("todoform.html")

#action route, default method is GET aka Display
@app.route("/todo/new", methods = [ 'POST' ])
def create_todo():
    print(request.form)
    new_todo = {
        "todo" : request.form["todo"],
        "status" : request.form["status"]
    }
    list_todos.append(new_todo)
    return redirect("/todos")



if __name__ == "__main__":
    app.run(debug = True)
#this code is needed to run your environment and be in an active state when you run this file.
#if you need to change the port, you add it to this statement with a ", port = 500x"

"""
Four methods:
GET - read and display
naming convention: what you are trying to display.
example: for all displays, maybe use /todos!
example: for individual displays, maybe use /todo/<int:id>!
example: /user/<int or str:id>

Function: get_all_todos()
Function: get_todo_by_id( id )

POST - create
naming convention: only doing one function, so be succinct. we are only creating something new.
example: "/todo/new"
example: "/user/new"

Function: create_user()
Function: create_todo()

PUT - update
naming convention: updating something already existing. Name of the object singularly that we are updating, followed by the id, followed by update or edit.
example: "/todo/<int:id>/edit"
example: "/user/<int or str:id>/update"

Function: update_user_by_id( id )
Function: update_todo_by_id( id )

DELETE - remove
naming convention: removing something already existing. Name of the object singularly that we are deleting, followed by the id, followed by delete or remove.
example: "/todo/<int:id>/delete"
example: "/user/<int or str:id>/remove"

Function: delete_user_by_id( id )
Function: delete_todo_by_id( id )
"""