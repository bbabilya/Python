from flask_app.config.mysqlconnection import connectToMySQL
#importing mysql connection to access database

from flask_app import DATABASE
#imports the schema under the variable DATABASE

class Ninja:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def show_one_dojo(cls,data):
        query = "SELECT * from ninjas"
        query += " WHERE dojo_id = %(dojo_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninjas_in_dojo = []

        print(results)

        for ninja in results:
            ninjas_in_dojo.append(ninja)
        
        print(ninjas_in_dojo)
        
        return ninjas_in_dojo

    @classmethod
    def add_one_ninja(cls, data):
        query = "INSERT into ninjas(first_name, last_name, age, dojo_id) "
        query +=" VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"

        return connectToMySQL(DATABASE).query_db(query, data)