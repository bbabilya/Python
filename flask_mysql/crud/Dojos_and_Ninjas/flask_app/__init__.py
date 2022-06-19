from flask import Flask
#import flask to your python file

app = Flask(__name__)
#call app name

DATABASE = 'dojos_and_ninjas_schema'
#defaults the variable DATABASE for your schema so you don't have to retype the schema every time. :) 