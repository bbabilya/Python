from flask_app.models.email import Email
from flask import render_template, redirect, request
from flask_app import app

##### DISPLAY ROUTES ######
@app.route("/")
def display_email_form():
    return render_template("email_form.html")

@app.route("/all_emails")
def display_all_emails():
    emails_list = Email.display_all_emails()

    return render_template("all_emails.html", emails_list = emails_list)

##### CREATE ROUTES ######
@app.route("/add_new_email", methods=['POST'])
def add_new_email():
    new_email = {
    'email_address' : request.form['email_address']
    }

    if not Email.validate_email(request.form):
        return redirect("/")

    else:
        Email.add_email(request.form)
        return redirect("/all_emails")

#### DELETE ROUTES ####
@app.route("/<int:id>/delete")
def delete_this_email(id):
    delete_email = {
        'id' : id
    }

    Email.delete_one_email(delete_email)
    return redirect("/all_emails")