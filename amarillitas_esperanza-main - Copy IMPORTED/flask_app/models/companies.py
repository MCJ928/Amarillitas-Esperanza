from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models.users import User


import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class Company:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.cuit = data['cuit']
        self.adress = data['adress']
        #Ariel Avila - 29-04-2024 MB01: Se agregan los campos faltantes de latitud y longitud
        self.adress_lat = data['adress_lat']
        self.adress_long = data['adress_long']
        self.description = data['description']
        self.phone = data['phone']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image = data['image']
        self.neighborhood = data['neighborhood']
        
        self.category_id = data['category_id']


    @classmethod
    def save(cls, form):
        #Ariel Avila - 29-04-2024 MB01: Se agregan los campos faltantes de latitud y longitud
        query = "INSERT INTO companies(image, name, cuit, adress, adress_lat, adress_long, description, phone, email, password, neighborhood, category_id) VALUES( %(image)s, %(name)s, %(cuit)s, %(adress)s, %(adress_lat)s, %(adress_long)s, %(description)s, %(phone)s, %(email)s, %(password)s, %(neighborhood)s, %(category_id)s)"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result
    
    
    @staticmethod
    def validate_company(form):
        is_valid = True
        if len(form['name']) <2:
            flash("Nombre debe tener al menos 2 caracteres", "register_company")
            is_valid = False
        
        if len(form['description']) <5:
            flash("Descripción debe tener al menos 5 caracteres", "register_company")
            is_valid = False
        
        if form['cuit'] == "":
            flash("CUIT no puede estar vacío", 'register_company')
            is_valid = False
        
        
        if not EMAIL_REGEX.match(form['email']):
            flash("Email inválido")
            is_valid = False
        
        query = "SELECT * FROM companies WHERE email = %(email)s"
        results = connectToMySQL('amarillitas').query_db(query, form)
        if len(results) >= 1:
            flash("Email registrado previamente", "register_company")
            is_valid = False

        if len(form['password']) < 6:
            flash("Contraseña debe tener al menos 6 caracteres", "register_company")
            is_valid = False

        password = form['password']
        if not any(p.isupper() for p in password) and not any(p.isdigit() for p in password):
            flash("Contraseña debe tener al menos un número y una mayuscula", "register_company")
            is_valid = False

        if form['password'] != form['confirm']:
            flash("Contraseñas no coinciden" , "register_company")
            is_valid = False
        
        return is_valid
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM companies"
        results = connectToMySQL('amarillitas').query_db(query)
        return results
        
    
    @classmethod
    def get_by_email(cls, form):
        query = "SELECT * FROM companies WHERE email = %(email)s"
        results = connectToMySQL('amarillitas').query_db(query, form)
        if len(results) == 1:
            company = cls(results[0])
            return company
        else:
            return False
    
    @classmethod
    def get_by_id(cls,form):
        query = "SELECT * FROM companies WHERE id = %(id)s"
        result = connectToMySQL('amarillitas').query_db(query, form)
        user = cls(result[0])
        return user
    
    
    @classmethod
    def get_by_category(cls, form):
        query = "SELECT * FROM companies JOIN categories ON categories.id = category_id WHERE category_id = %(category_id)s"
        result = connectToMySQL('amarillitas').query_db(query,form)
        companies = []
        for company in result:
            companies.append(cls(company))
        return companies
    
    @classmethod
    def get_by_points(cls):
        query= "SELECT companies.id, companies.name, companies.image, round(avg(stars.points), 1) AS points FROM companies JOIN stars ON companies.id = company_id GROUP BY companies.id ORDER BY points desc LIMIT 6;"
        result = connectToMySQL('amarillitas').query_db(query)
        return result
    
    
    @classmethod
    def company_points(cls,form):
        query= "SELECT companies.id, companies.name, round(avg(stars.points), 1) AS points FROM companies LEFT JOIN stars ON companies.id = company_id WHERE companies.id = %(id)s GROUP BY companies.id"
        result = connectToMySQL('amarillitas').query_db(query,form)
        return result
    
    
    @classmethod
    def update(cls, form):
        query = "UPDATE companies SET name=%(name)s, description=%(description)s, cuit=%(cuit)s, email=%(email)s, phone=%(phone)s, adress=%(adress)s, adress_lat=%(adress_lat)s, adress_long=%(adress_long)s, category_id=%(category_id)s, neighborhood=%(neighborhood)s WHERE id= %(id)s"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result
    
    
    @classmethod
    def login(cls,form):
        query = "SELECT users.email, users.password, companies.email, companies.password FROM amarillitas.users, amarillitas.companies;"
        results = connectToMySQL('amarillitas').query_db(query, form)
        return results


    @classmethod
    def get_by_search(cls, form):
        query = "SELECT * FROM companies WHERE name LIKE '%()s'"
        results = connectToMySQL('amarillitas').query_db(query, form)
        return results
    
    
    @classmethod
    def get_by_neighborhood(cls, form):
        query = "SELECT * FROM companies WHERE neighborhood= %(neighborhood)s"
        result = connectToMySQL('amarillitas').query_db(query,form)
        companies = []
        for company in result:
            companies.append(cls(company))
        return companies