from flask_app.controllers import dojos
from flask_app.controllers import ninjas
#importing the Dojos controller into our server.py
#importing the Ninjas controller into our server.py
from flask_app import app
#importing the app name

if __name__ == "__main__":
    app.run(debug = True)

#app debug statement to run server