from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Magazine:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_magazine(cls, data):
        query = "INSERT INTO magazines(name, description, user_id) "
        query += " VALUES(%(name)s, %(description)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_magazine(cls, data):
        query = "SELECT * FROM magazines "
        query += " JOIN users ON users.id = magazines.user_id "
        query += " WHERE magazines.id = %(id)s ;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        
        if len(results) < 1:
            return False
        
        return cls(results[0])
    
    @classmethod
    def get_all_magazines(cls):
        query = "SELECT * FROM magazines "
        query += " JOIN users ON users.id = magazines.user_id ; "

        results = connectToMySQL(DATABASE).query_db(query)
        
        all_magazines = []
        
        for magazine in results:
            all_magazines.append(cls(magazine))

        return all_magazines

    @classmethod
    def edit_magazine(cls, data):
        query = "UPDATE magazines "
        query += " SET name = %(name)s, description = %(description)s "
        query += " WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one_magazine(cls, data):
        query = "DELETE FROM magazines "
        query += " WHERE id = %(id)s; "
    
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_user_magazines(cls, data):
        query = "SELECT * FROM magazines "
        query += " JOIN users ON users.id = magazines.user_id "
        query += "WHERE user_id = %(id)s"
        
        return connectToMySQL(DATABASE).query_db(query, data)

