from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add_email(cls, data):
        query = "INSERT into email(email_address) "
        query += " VALUES(%(email_address)s);"

        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def display_all_emails(cls):
        query = "SELECT * "
        query += " from email;"
        results = connectToMySQL(DATABASE).query_db(query)

        all_emails = []

        for email in results:
            all_emails.append(email)

        return all_emails

    @classmethod
    def delete_one_email(cls, data):
        query = "DELETE FROM email "
        query += " WHERE ID = %(id)s;"
        
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def unique_email(cls, data):
        query = "SELECT * FROM email "
        query += " WHERE email_address = %(email_address)s"
        
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate_email(email):
        is_valid = True

        if Email.unique_email(email):
            flash("Email is already in use!")
            is_valid = False

        elif not EMAIL_REGEX.match(email['email_address']):
            flash("Email Address is not valid!")
            is_valid = False

        else:
            flash(f"The email address you entered ({email['email_address']}) is a VALID email address! Thank you!")
        return is_valid
