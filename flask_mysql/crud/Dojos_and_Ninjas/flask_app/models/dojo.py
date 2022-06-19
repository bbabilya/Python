from flask_app.config.mysqlconnection import connectToMySQL
#importing mysql connection to access database

from flask_app import DATABASE
#imports the schema under the variable DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * "
        query += " FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        #results will be a list of dictionaries containing information from each row
        
        all_dojos = []
        #empty list for appending information

        for dojo in results:
            #forloop for looping through the dictionaries provided by MYSQL
            all_dojos.append(dojo)
            #appending the information provided from the forloop into the list
        return all_dojos

    @classmethod
    def add_one_dojo(cls, data):
        query = "INSERT into dojos(name)"
        query += "VALUES(%(name)s);"

        return connectToMySQL(DATABASE).query_db(query, data)



