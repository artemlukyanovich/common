from flask import Blueprint
from flask_restful import Api
from routes.tenants.resource import Tenants

api_bp = Blueprint('tenants', __name__)
api = Api(api_bp)

api.add_resource(Tenants, '/tenants', '/tenants/<value>')

