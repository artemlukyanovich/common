import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse


class Room:
    def __init__(self, number: int, level: str, status: str, price: int):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms_list = list()
rooms_list.append(Room(21, "Lux", "Not available", 200))
rooms_list.append(Room(32, "Standard", "Not available", 100))
rooms_list.append(Room(33, "Standard", "Available", 100))

room_structure = {
    "number": fields.Integer,
    "level": fields.String(default="Standard"),
    "status": fields.String(default="Available"),
    "price": fields.Integer
}

status_list = ["Available", "Not available"]

parser = reqparse.RequestParser()
parser.add_argument("status", type=str, help="Please enter the correct status!")


class Rooms(Resource):
    def get(self, value=None):
        @marshal_with(room_structure)  # show() function to make messages correct
        def show(x):
            return x
        args = parser.parse_args()
        if args['status']:
            status = args['status'].replace("_", " ")
            result = list()
            for room in rooms_list:
                if room.status == status:
                    result.append(room)
            return show(result)
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for room in rooms_list:
                if room.number == value:
                    return show(room)
            return "There is no such room!"
        return show(rooms_list)

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
            return "Is Available or Not available?"
        for room in rooms_list:
            if room.number == number:
                return "Oops! Such room already exists!"
        rooms_list.append(Room(number, level, status, price))
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
            for room in rooms_list:
                if room.number == value:
                    rooms_list.remove(room)
                    rooms_list.append(Room(number, level, status, price))
                    return "Successfully updated!"
            return "There is no such room!"
        return "Please choose the room!"


    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for room in rooms_list:
                if room.number == value:
                    rooms_list.remove(room)
                    return "Successfully removed!"
            return "There is no such room!"
        return "Please choose the room!"



