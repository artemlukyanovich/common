from flask import Blueprint
from flask_restful import Api
from routes.rooms.resource import Rooms

api_bp = Blueprint('rooms', __name__)
api = Api(api_bp)

api.add_resource(Rooms, '/rooms', '/rooms/<value>')

