from flask import request, flash
from usuarios_app.config.mysqlconnection import connectToMySQL

DATABASE_NAME = 'esquema_dojos_y_ninjas'

class Dojo:
    def __init__(self, data):
        self.nombre=data['nombre']

    @classmethod
    def getAll(cls):
        query="""
        SELECT * FROM dojos
        """
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        print("RESULTSSSSS",results)
        dojos=[]
        for dojo in results:
            dojos.append(cls(dojo))
        return results

    @classmethod
    def new(cls, data):
        query = """
        INSERT INTO dojos(nombre)
         VALUES (%(nombre)s);
        """
        resultado = connectToMySQL(DATABASE_NAME).query_db(query, data)
        print(resultado, "*/"*10)
        return resultado

    @classmethod
    def getOne(cls,data):
        query="""
        SELECT * FROM dojos WHERE id = %(id)s
        """
        results = connectToMySQL(DATABASE_NAME).query_db(query,data)
        print("RESULTSSSSS:",results)
        return results

    
    
