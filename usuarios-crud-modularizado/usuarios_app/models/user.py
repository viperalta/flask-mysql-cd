from unittest import result
from flask import request, flash
from usuarios_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.first_name=data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def getAll(cls):
        query="""
        SELECT * FROM users
        """
        results = connectToMySQL('esquema_usuarios').query_db(query)
        print("RESULTSSSSS",results)
        users=[]
        for user in results:
            users.append(cls(user))
        return results

    @classmethod
    def new(cls, data):
        query = """
        INSERT INTO users(first_name, last_name, email)
         VALUES (%(first_name)s,%(last_name)s, %(email)s);
        """
        resultado = connectToMySQL('esquema_usuarios').query_db(query, data)
        print(resultado, "*/"*10)
        return resultado

    @classmethod
    def getOne(cls,data):
        query="""
        SELECT * FROM users WHERE id = %(id)s
        """
        results = connectToMySQL('esquema_usuarios').query_db(query,data)
        print("RESULTSSSSS:",results)
        return results

    @classmethod
    def edit(cls,data):
        query="""
        UPDATE users 
        SET first_name = %(first_name)s,last_name = %(last_name)s, email = %(email)s, updated_at = NOW()
        WHERE id = %(id)s
        """
        results = connectToMySQL('esquema_usuarios').query_db(query,data)
        print("EDIIIIT",results)
        return results

    @classmethod
    def delete(cls,data):
        query="""
        DELETE FROM users WHERE id = %(id)s
        """
        results = connectToMySQL('esquema_usuarios').query_db(query,data)
        print("EDIIIIT",results)
        return results