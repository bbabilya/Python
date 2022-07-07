from flask import Flask
from flask import flash, session


app = Flask(__name__)
app.secret_key = "secrets"

DATABASE = 'sponsorship_schema'