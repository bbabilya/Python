from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "montyPython"

@app.route("/")
def start_page():
    return render_template("index.html")


@app.route("/button_click")
def add_click():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
    return redirect("/")

@app.route("/destroy_session")
def reset_session():
        session.clear()
        session["num_of_visits"] = 0
        return redirect("/")

@app.route("/add_session")
def add_to_session():
    if "num_of_visits" in session:
        session["num_of_visits"] += 2
    else:
        session["num_of_visits"] = 2
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)