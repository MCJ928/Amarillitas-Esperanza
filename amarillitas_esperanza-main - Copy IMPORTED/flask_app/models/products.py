from flask_app.config.mysqlconnection import connectToMySQL


from flask import flash


class Product:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.image = data['image']
        
        self.company_id = data['company_id']


    @classmethod
    def save(cls, form):
        query = "INSERT INTO products ( name, description, company_id, image) VALUES(%(name)s, %(description)s, %(company_id)s, %(image)s);"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result


    @staticmethod
    def validate_product(form):
        is_valid = True
        
        if len(form['name']) <2:
            is_valid = False
        
        if len(form['description']) <5:
            is_valid = False
            
        return is_valid


    @classmethod
    def get_by_company_id(cls,form):
        query = "SELECT * FROM products WHERE company_id = %(id)s ORDER BY updated_at DESC"
        result = connectToMySQL('amarillitas').query_db(query, form)
        products = []
        for product in result:
            products.append(cls(product))
        return products

    @classmethod
    def get_all(cls):
        query = "SELECT products.* FROM products ORDER BY updated_at DESC"
        results = connectToMySQL('amarillitas').query_db(query)
        products = []
        for product in results:
            products.append(cls(product))
        return products

    @classmethod
    def get_by_id(cls,form):
        query = "SELECT * FROM products WHERE id = %(id)s"
        result = connectToMySQL('amarillitas').query_db(query,form)
        product = cls(result[0])
        return product


    @classmethod
    def get_by_updated(cls):
        query = "SELECT * FROM products ORDER BY updated_at DESC LIMIT 5;"
        results = connectToMySQL('amarillitas').query_db(query)
        products = []
        for product in results:
            products.append(cls(product))
        return products

    @classmethod
    def update(cls, form):
        query = "UPDATE products SET name=%(name)s, description=%(description)s WHERE id=%(id)s;"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result


    @classmethod
    def delete_product(cls,form):
        query = "DELETE FROM products WHERE id = %(id)s"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result