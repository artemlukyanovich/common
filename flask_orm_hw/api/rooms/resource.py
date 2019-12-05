import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from db import Rooms, db

room_structure = {
    "number": fields.Integer,
    "level": fields.String(default="Standard"),
    "status": fields.String(default="Available"),
    "price": fields.Integer,
    "tenant_id": fields.Integer(default="No tenants")
}

status_list = ["Available", "Not available"]

parser = reqparse.RequestParser()
parser.add_argument("status", type=str, help="Please enter the correct status!")


class RoomsRes(Resource):
    def get(self, value=None):
        @marshal_with(room_structure)  # show() function to make messages correct
        def show(x):
            return x

        args = parser.parse_args()
        if args['status']:
            status = args['status'].replace("_", " ")
            result = Rooms.query.filter_by(status=status)
            return show(result)
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            result = Rooms.query.get(value)
            if not result:
                return "Oops! There is no such room!"
            return show(result)
        return show(Rooms.query.all())

    def post(self):
        data = json.loads(request.data)
        number = data.get('number')
        level = data.get('level')
        status = data.get('status')
        price = data.get('price')
        tenant_id = data.get('tenant_id')
        if number is None:
            return 'Please enter the correct number!'
        elif not type(number) == int and not number.isdigit():
            return 'Please enter the correct number!'
        if Rooms.query.get(number):
            return "Oops! Such room already exists!"
        if status not in status_list and status is not None:
            return "Is it Available or Not available?"
        if price is None:
            return 'Please enter the correct price!'
        elif not type(price) == int and not price.isdigit():
            return 'Please enter the correct price!'
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
        except ValueError:
            return "Please enter the correct data!"
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            room_prev = Rooms.query.get(value)
            if not room_prev:
                return "Oops! There is no such room!"
            if Rooms.query.get(number):
                return "Oops! This Number is not available!"
            db.session.delete(room_prev)
            room_new = Rooms(**data)
            db.session.add(room_new)
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
