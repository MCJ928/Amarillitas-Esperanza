from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models.companies import Company


class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM categories"
        results = connectToMySQL('amarillitas').query_db(query)
        categories = []
        for category in results:
            categories.append(cls(category))
        return categories
    
    @classmethod
    def get_by_id(cls, form):
        query = "SELECT * FROM categories WHERE id = %(id)s"
        result = connectToMySQL('amarillitas').query_db(query, form)
        category = cls(result[0])
        return category
    
    
    @classmethod
    def get_by_company_id(cls, form):
        query = "SELECT categories.*, companies.id FROM categories JOIN companies ON categories.id = category_id WHERE companies.id = %(id)s"
        result = connectToMySQL('amarillitas').query_db(query,form)
        return result
