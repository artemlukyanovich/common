from flask import Blueprint
from flask_restful import Api
from routes.staff.resource import Staff

api_bp = Blueprint('staff', __name__)
api = Api(api_bp)

api.add_resource(Staff, '/staff', '/staff/<value>')

