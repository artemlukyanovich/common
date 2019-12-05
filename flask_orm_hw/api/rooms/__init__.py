from flask import Blueprint
from flask_restful import Api
from api.rooms.resource import RoomsRes

api_bp = Blueprint('rooms', __name__)
api = Api(api_bp)

api.add_resource(RoomsRes, '/rooms', '/rooms/<value>')

