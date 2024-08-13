from flask_app.config.mysqlconnection import connectToMySQL


class Star:
    def __init__(self,data):
        self.id = data['id']
        self.points = data['points']
        self.user_id = data['user_id']
        self.company_id = data['company_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, form):
        query = "INSERT INTO stars (points, user_id, company_id) VALUES (%(points)s, %(user_id)s, %(company_id)s)"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result

