from flask_app.config.mysqlconnection import connectToMySQL


class Comment:
    def __init__(self,data):
        self.id = data['id']
        self.text = data['text']
        self.user_id = data['user_id']
        self.company_id = data['company_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, form):
        query = "INSERT INTO comments (text, user_id, company_id) VALUES (%(text)s, %(user_id)s, %(company_id)s)"
        result = connectToMySQL('amarillitas').query_db(query, form)
        return result
    
    @classmethod
    def get_by_company_id(cls,form):
        query = "SELECT * FROM comments WHERE company_id = %(id)s ORDER BY updated_at DESC"
        result = connectToMySQL('amarillitas').query_db(query, form)
        comments = []
        for comment in result:
            comments.append(cls(comment))
        return comments

