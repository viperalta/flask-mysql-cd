from flask import request, flash
from usuarios_app.config.mysqlconnection import connectToMySQL

DATABASE_NAME = 'esquema_dojos_y_ninjas'

class Ninja:
    def __init__(self, data):
        self.first_name=data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']

    @classmethod
    def new(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name,age,dojo_id)
        VALUES (%(first_name)s,%(last_name)s, %(age)s, %(dojo_id)s);
        """
        resultado = connectToMySQL(DATABASE_NAME).query_db(query, data)
        print(resultado, "*/"*10)
        return resultadoç

    @classmethod
    def getNinjas(cls,data):
        query="""
        SELECT * FROM ninjas WHERE dojo_id = %(id)s
        """
        results = connectToMySQL(DATABASE_NAME).query_db(query,data)
        ninjas=[]
        for ninja in results:
            ninjas.append(cls(ninja))
        return results