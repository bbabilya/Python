# import the function for mysql
from flask_app.config.mysqlconnection import connectToMySQL

# class model for users
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    #class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # query call
        results = connectToMySQL('users_schema').query_db(query)
        # empty list
        users = []
        # for loop to iterate over rows
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email)"
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        print(query)
        result = connectToMySQL('users_schema').query_db(query, data)
        print(result)
        return cls(result[0])

    @classmethod
    def edit_one_user(cls, data):
        query = "UPDATE users "
        query += "SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s "
        query += " WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query, data)
        return(result)

    @classmethod
    def delete_one_user(cls, data):
        query = "DELETE FROM users "
        query += "WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return(result)