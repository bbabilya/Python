from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.cooking_time = data['cooking_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, date_made, cooking_time, user_id) "
        query += " VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(cooking_time)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * from recipes "
        query += " WHERE id = %(id)s"

        results = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(results) < 1:
            return False
        
        return cls(results[0])
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes "

        results = connectToMySQL(DATABASE).query_db(query)
        
        all_recipes = []
        
        for recipe in results:
            all_recipes.append(recipe)

        return all_recipes

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes "
        query += " SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, cooking_time = %(cooking_time)s "
        query += " WHERE id = %(id)s; "
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one_recipe(cls, data):
        query = "DELETE FROM recipes "
        query += " WHERE id = %(id)s; "
    
        return connectToMySQL(DATABASE).query_db(query, data)
