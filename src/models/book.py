from flask_restplus import fields
from server.instance import server

book = server.api.model('Book', {
    'id': fields.Integer(description='Id'),
    'title': fields.String(required=True, min_length=1, max_length=200, description='Book title'),
    'author': fields.String(required=False, min_length=1, max_length=200, description='Book author'),
    'year': fields.Integer(required=False, min_length=4, max_length=4, description='Year of Publishing'),
    'country': fields.String(required=False, min_length=1, max_length=100, description='Country Origin')
})
