from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keepitsafe"

@app.route ("/")
def display_create_survey():
    return render_template("index.html")


@app.route ("/survey/new", methods=['POST'])
def create_survey():
    print("Hello World :)")
    session["new_survey"] = {
        "name" : request.form["name"],
        "dojo_location" : request.form["dojo_location"],
        "favorite_language" : request.form["favorite_language"],
        "comments" : request.form["comments"],
    }
    return redirect("/survey/results")

@app.route("/survey/results")
def display_survey():
    return render_template("result.html")





if __name__ == "__main__":
    app.run(debug = True)
