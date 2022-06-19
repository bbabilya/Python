from mysqlconnection import connectToMySQL

# DEFINE USER CLASS
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# GETS ALL USERS AND ALL USER INFORMATION EXCEPT UPDATED_BY COL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

# CREATES USER WITH QUERY VALUES
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email)"
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s)"

        result = connectToMySQL('users_schema').query_db(query, data)


