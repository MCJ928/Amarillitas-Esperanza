from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash


import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, form):
        query = "INSERT INTO users ( first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result

    @staticmethod
    def validate_user(form):
        is_valid = True
        if len(form['first_name']) <2:
            flash("Nombre debe tener al menos 2 caracteres", "register")
            is_valid = False
        
        if len(form['last_name']) <2:
            flash("Apellido debe tener al menos 2 caracteres", "register")
            is_valid = False
        
        if not EMAIL_REGEX.match(form['email']):
            flash("Email inválido")
            is_valid = False
        
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('amarillitas').query_db(query, form)
        if len(results) >= 1:
            flash("Email registrado previamente", "register")
            is_valid = False

        if len(form['password']) < 6:
            flash("Contraseña debe tener al menos 6 caracteres", "register")
            is_valid = False

        password= form['password']
        if not any(p.isupper() for p in password) and not any(p.isdigit() for p in password):
            flash("Contraseña debe tener al menos un número y una mayuscula", "register")
            is_valid = False

        if form['password'] != form['confirm_u']:
            flash("Contraseñas no coinciden" , "register")
            is_valid = False
        
        return is_valid
    

    @classmethod
    def get_by_email(cls, form):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('amarillitas').query_db(query, form)
        if len(results) == 1:
            user = cls(results[0])
            return user
        else:
            return False

    @classmethod
    def get_by_id(cls,form):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('amarillitas').query_db(query, form)
        user = cls(result[0])
        return user
    
    @classmethod
    def update(cls, form):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result
    

