from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app import app
import re	


class Child:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.country = data['country']
        self.about_me = data['about_me']
        self.siblings = data['siblings']
        self.risk_category = data['risk_category']


@classmethod
def get_all_children(cls):
    query = "SELECT * "
    query += " FROM children; "

    results = connectToMySQL(DATABASE).query_db(query)
    all_children = []

    for child in results:
        all_children.append(cls(child))
    
    return all_children

@classmethod
def get_children_by_country(cls):
    query = "SELECT * "
    query += " FROM children "
    query += " WHERE country = %(country)s; "

    results = connectToMySQL(DATABASE).query_db(query)
    all_children = []

    for child in results:
        all_children.append(cls(child))
    
    return all_children

@classmethod
def get_children_by_country(cls):
    query = "SELECT * "
    query += " FROM children "
    query += " WHERE risk_cateogry = %(risk_category)s; "

    results = connectToMySQL(DATABASE).query_db(query)
    all_children = []

    for child in results:
        all_children.append(cls(child))
    
    return all_children