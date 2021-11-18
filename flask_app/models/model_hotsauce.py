##### Rename model_"name" to reflect project #####

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
# from flask_bcrypt import Bcrypt

# import re	# the regex module
# # create a regular expression object that we'll use later   
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# bcrypt = Bcrypt(app)

##### rename 'schema_name' #####
DATABASE_SCHEMA = 'hotsauce_db'
##### RENAME: class_name(cap first letter), DATABASE_SCHEMA ##### 
##### hotsauces, column_name, all_hotsauces, new_hotsauces_id #####

class Hotsauce:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ferment_start = data['ferment_start']
        self.ferment_ingredients = data['ferment_ingredients']
        self.process_date = data['process_date']
        self.process_ingredients = data['process_ingredients']
        self.process_notes = data['process_notes']
        self.description = data['description']
        self.completed = data['completed']
        self.favorite = data['favorite']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# C **************************************************
# C **************************************************
# C **************************************************


    @classmethod
    def create_ferment(cls, data):
        query = 'INSERT INTO hotsauces (name, ferment_start, ferment_ingredients ) VALUES (%(name)s, %(ferment_start)s, %(ferment_ingredients)s)'
        new_ferment_id = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)

        return new_ferment_id
    
    # @classmethod
    # def create_hotsauce(cls, data):
    #     query = 'INSERT INTO hotsauces (process_date, process_ingredients, process_notes, description, completed, favorite ) VALUES (%(process_date)s, %(process_ingredients)s, %(process_notes)s,  %(description)s,  %(completed)s,  %(favorite)s)'
    #     new_hotsauces_id = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)

    #     return new_hotsauces_id


# R **************************************************
# R **************************************************
# R **************************************************


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM hotsauces;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        all_hotsauces = []
        for hotsauces in results:
            all_hotsauces.append(cls(hotsauces))  ### remane cls to CLASS assigned
        return all_hotsauces


    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM hotsauces WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if not results:
            return results
        return cls(results[0])


    ############# VALIDATIONS #############


    # @classmethod
    # def get_by_id(cls, data):
    #     query = 'SELECT * FROM hotsauces WHERE id = %(id)s;'
    #     results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
    #     if len(results) < 1:
    #         return False

    #     return Hotsauce(results[0])


    # @classmethod
    # def get_by_email(cls, data):
    #     query = 'SELECT * FROM hotsauces WHERE email = %(email)s;'
    #     results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
    #     if len(results) < 1:
    #         return False

    #     return Hotsauce(results[0])


# U **************************************************
# U **************************************************
# U **************************************************


    @classmethod
    def update_one(cls, data):
        query = 'UPDATE hotsauces SET process_date = %(process_date)s, process_ingredients = %(process_ingredients)s, process_notes = %(process_notes)s, description = %(description)s, completed = %(completed)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    @classmethod
    def update_hotsauce(cls, data):
        query = 'UPDATE hotsauces SET name = %(name)s, ferment_start = %(ferment_start)s, ferment_ingredients = %(ferment_ingredients)s, process_date = %(process_date)s, process_ingredients = %(process_ingredients)s, process_notes = %(process_notes)s, description = %(description)s, completed = %(completed)s WHERE id = %(id)s'
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

# D **************************************************
# D **************************************************
# D **************************************************


    # @classmethod
    # def delete_one(cls, **data):
    #     query = 'DELETE FROM hotsauces WHERE id = %(id)s'
    #     connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
    #     return id


# **************** VALIDATIONS GO HERE****************
