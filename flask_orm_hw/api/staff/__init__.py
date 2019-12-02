from flask import Blueprint
from flask_restful import Api
from api.staff.resource import StaffRes

api_bp = Blueprint('staff', __name__)
api = Api(api_bp)

api.add_resource(StaffRes, '/staff', '/staff/<value>')

