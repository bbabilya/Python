from flask_app.models.child import Child
from flask import render_template, redirect, request, session
from flask_app import app
from flask import flash


@app.route("/")
def display_main_page():
    return render_template("index.html")

@app.route("/child/new")
def display_child_form():
    return render_template("child_form.html")