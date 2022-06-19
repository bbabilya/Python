from flask import Flask, render_template

#Project by Kaija Pendergast and Brandi Babilya

app = Flask(__name__)


@app.route ("/") 
@app.route ("/<int:column>") 
@app.route ("/<int:column>/<int:row>") 
@app.route ("/<int:column>/<int:row>/<string:color1>")
@app.route ("/<int:column>/<int:row>/<string:color1>/<string:color2>")
#All columns, rows and colors declared
def get_new_columns_and_colors(column = 8,row = 8,color1 = "black",color2 = "red"):
    return render_template("index.html", color1 = color1, color2 = color2, column = int(column), row = int(row))


if __name__ == "__main__":
    app.run(debug = True)
