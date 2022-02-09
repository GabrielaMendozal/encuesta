from encuesta_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, id,name,location,language,comment, created_at,updated_at):
        self.id = id
        self.name = name 
        self.location = location
        self.language = language
        self.comment = comment
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def agregar(cls, nuevoDojo):
        query = "INSERT INTO dojos (name, location,language,comment) VALUES (%(name)s, %(location)s,%(language)s,%(comment)s);"
        resultado = connectToMySQL ("encuesta").query_db (query,nuevoDojo)

    @classmethod
    def obtenerDatosDojos(cls):
        query = "SELECT * FROM dojos ;"
        resultado = connectToMySQL ("encuesta").query_db(query)
        print (type (resultado), "QUE SOY YO ")
        return resultado [0]

    


    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # asumimos que esto es true
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 5:
            flash("Location must be at least 5 characters.")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("Language must be at least 2 characters.")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Comment must be at least 10 characters.")
            is_valid = False
        return is_valid             