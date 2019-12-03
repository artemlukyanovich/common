import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from db import Rooms, db

room_structure = {
    "number": fields.Integer,
    "level": fields.String(default="Standard"),
    "status": fields.String(default="Available"),
    "price": fields.Integer
}

# rooms_list = list()
# rooms_list.append(Room(21, "Lux", "Not available", 200))
# rooms_list.append(Room(32, "Standard", "Not available", 100))
# rooms_list.append(Room(33, "Standard", "Available", 100))

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
            result = Rooms.query.filter_by(number=value)
            if not result.count():
                return "Oops! There is no such room!"
            return show(result.all())
        return show(Rooms.query.all())

    def post(self):
        data = json.loads(request.data)
        try:
            number = int(data.get('number'))
            level = str(data.get('level'))
            status = str(data.get('status'))
            price = int(data.get('price'))
        except ValueError:
            return "Please enter the correct data!"
        if status not in status_list:
            return "Is it Available or Not available?"
        if Rooms.query.filter_by(number=number).count():
            return "Oops! Such room already exists!"
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
            room_prev = Rooms.query.filter_by(number=value)
            if not room_prev.count():
                return "Oops! There is no such room!"
            if Rooms.query.filter_by(number=number).count():
                return "Oops! This Number is not available!"
            db.session.delete(room_prev.first())
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
            room = Rooms.query.filter_by(number=value)
            if room.count():
                db.session.delete(room.first())
                db.session.commit()
                return "Successfully removed!"
            return "Oops! There is no such room!"
        return "Please choose the room!"



