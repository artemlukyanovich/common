from flask import Blueprint
from flask_restful import Api
from api.tenants.resource import TenantsRes

api_bp = Blueprint('tenants', __name__)
api = Api(api_bp)

api.add_resource(TenantsRes, '/tenants', '/tenants/<value>')

