import json
from flask import request
from flask_restful import Resource, fields, marshal_with

rooms_list = list()


class Room:
    def __init__(self, number: int, level: str, status: str, price: int):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms_list.append(Room(21, "Lux", "Not available", 200))
rooms_list.append(Room(32, "Standard", "Available", 100))

room_structure = {
    "number": fields.Integer,
    "level": fields.String(default="Standard"),
    "status": fields.String(default="Available"),
    "price": fields.Integer
}


class Rooms(Resource):
    @marshal_with(room_structure)
    def get(self):
        return rooms_list

    def post(self):
        data = json.loads(request.data)
        try:
            number = int(data.get('number'))
            level = str(data.get('level'))
            status = str(data.get('status'))
            price = int(data.get('price'))
        except ValueError:
            return "Please enter the correct data!"
        for room in rooms_list:
            if room.number == number:
                return "Oops! Such room already exists!"
        rooms_list.append(Room(number, level, status, price))
        return "Successfully added!"


#     def patch(self):
# """Make with break if there is a *number*
# if not - return that there is no such room"""
#         pass

