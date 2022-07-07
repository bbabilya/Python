from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
import re	

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.magazines = []

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, password) "
        query += " VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def unique_email(cls, data):
        query = "SELECT * from users "
        query += " WHERE email = %(email)s"
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(result) < 1:
            return False
        
        return cls(result[0])

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * from users "
        query += " WHERE id = %(id)s; "

        results = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(results) < 1:
            return False
        
        return cls(results[0])

    @classmethod
    def edit_one_user(cls, data):
        query = "UPDATE users "
        query += "SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s "
        query += " WHERE id = %(id)s ;"

        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate_user(users):
        is_valid = True

        if User.unique_email(users):
            flash("Email is already in use!", 'email_error')
            is_valid = False

        elif not EMAIL_REGEX.match(users['email']):
            flash("Email Address is not valid!", 'email_error')
            is_valid = False
        
        else:
            return is_valid

    @classmethod
    def get_user_magazines(cls, data):
        query = "SELECT * FROM users "
        query += " JOIN magazines ON users.id = magazines.user_id WHERE users.id = %(id)s ;"

        results = connectToMySQL(DATABASE).query_db(query, data)

        print(results)
        return 

