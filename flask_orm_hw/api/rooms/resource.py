import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from db import Rooms, db, Tenants

staff_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "position": fields.String
}

room_structure1 = {
    "number": fields.Integer,
    "level": fields.String(default="Standard"),
    "status": fields.String(default="Available"),
    "price": fields.Integer,
    "tenant_id": fields.Integer(default="No tenants")
}

room_structure2 = {
    "number": fields.Integer,
    "level": fields.String(default="Standard"),
    "status": fields.String(default="Available"),
    "price": fields.Integer,
    "tenant_id": fields.Integer(default="No tenants"),
    "staff": fields.Nested(staff_structure)
}

status_list = ["Available", "Not available"]

parser = reqparse.RequestParser()
parser.add_argument("status", type=str, help="Please enter the correct status!")


class RoomsRes(Resource):
    def get(self, value=None):
        @marshal_with(room_structure1)  # show() function to make messages correct
        def show1(x):
            return x

        @marshal_with(room_structure2)  # show2() to see the room's staff
        def show2(x):
            return x

        args = parser.parse_args()
        if args['status']:
            status = args['status'].replace("_", " ")
            result = Rooms.query.filter_by(status=status).all()
            return show1(result)
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            result = Rooms.query.get(value)
            if not result:
                return "Oops! There is no such room!"
            return show2(result)
        return show1(Rooms.query.all())

    def post(self):
        try:
            data = json.loads(request.data)
            number = int(data.get('number'))
            level = data.get('level')
            status = data.get('status')
            price = int(data.get('price'))
            tenant_id = data.get('tenant_id')
        except ValueError:
            return "Please enter the correct data!"
        if Rooms.query.get(number):
            return "Oops! Such room already exists!"
        if status not in status_list and status is not None:
            return "Is it Available or Not available?"
        tenant = Tenants.query.get(tenant_id)
        if not tenant:
            return "Oops! There is no such tenant!"
        room = Rooms(**data)
        db.session.add(room)
        db.session.commit()
        return "Successfully added!"

    def patch(self, value=None):
        data = json.loads(request.data)
        try:
            number = int(data.get('number'))
            level = str(data.get('level'))
            status = str(data.get('status'))
            price = int(data.get('price'))
            tenant_id = data.get('tenant_id')
        except ValueError:
            return "Please enter the correct data!"
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            room = Rooms.query.get(value)
            if not room:
                return "Oops! There is no such room!"
            if value != number:
                return "You can't change room number!"
            if status not in status_list and status is not None:
                return "Is it Available or Not available?"
            tenant = Tenants.query.get(tenant_id)
            if not tenant:
                return "Oops! There is no such tenant!"
            room.level = level
            room.status = status
            room.price = price
            room.tenant_id = tenant_id
            db.session.commit()
            return "Successfully updated!"
        return "Please choose the room!"

    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            room = Rooms.query.get(value)
            if room:
                db.session.delete(room)
                db.session.commit()
                return "Successfully removed!"
            return "Oops! There is no such room!"
        return "Please choose the room!"
