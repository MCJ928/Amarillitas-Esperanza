from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Adress:
    def __init__(self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.company = data['company']

    @classmethod
    def get_adress(cls):
        query = "SELECT adress FROM adresses JOIN companies ON company_id = companies.id;"
        results = connectToMySQL('amarillitas').query_db(query)
        adresses = []
        for adress in results:
            adresses.append(cls(adress))
        return adresses

    