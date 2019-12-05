import json
from flask import request
from flask_restful import Resource, fields, marshal_with
from db import Staff, db, Rooms

rooms_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "price": fields.Integer
}

"""Separate structure to make it easier in hw to copy-past and post a new record"""
staff_structure1 = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}

staff_structure2 = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Integer,
    "rooms": fields.Nested(rooms_structure)
}


class StaffRes(Resource):
    def get(self, value=None):
        @marshal_with(staff_structure1)  # show() function to make messages correct
        def show1(x):
            return x

        @marshal_with(staff_structure2)
        def show2(x):   # show2() to see the employee's rooms
            return x

        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            result = Staff.query.get(value)
            if not result:
                return "Oops! There is no such employee!"
            return show2(result)
        return show1(Staff.query.all())

    def post(self, value=None):
        data = json.loads(request.data)

        if value:   # The room for the staff should be added here
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.get(value)
            if not empl:
                return "Oops! There is no such employee!"
            room_num = data.get('room_number')
            if room_num is None:
                return 'Please enter the correct room_number!'
            elif not type(room_num) == int and not room_num.isdigit():
                return 'Please enter the correct room_number!'
            room = Rooms.query.get(room_num)
            if not room:
                return "Oops! There is no such room!"
            empl.rooms.append(room)
            db.session.commit()
            return "Successfully added!"

        try:
            name = str(data.get('name'))  # too long :(
            passport_id = int(data.get('passport_id'))
            position = str(data.get('position'))
            salary = int(data.get('salary'))
        except ValueError:
            return "Please enter the correct data!"
        if Staff.query.get(passport_id):
            return "Oops! Such employee already exists!"
        empl = Staff(**data)
        db.session.add(empl)
        db.session.commit()
        return "Successfully added!"

    def patch(self, value=None):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
            passport_id = int(data.get('passport_id'))
            position = str(data.get('position'))
            salary = int(data.get('salary'))
        except ValueError:
            return "Please enter the correct data!"
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.get(value)
            if not empl:
                return "Oops! There is no such employee!"
            if value != passport_id:
                return "You can't change password ID!"
            empl.name = name
            empl.position = position
            empl.salary = salary
            db.session.commit()
            return "Successfully updated!"
        return "Please choose the employee!"

    def delete(self, value=None, value2=None):
        if value and value2:    # The room for the staff should be removed here
            try:
                value = int(value)
                value2 = int(value2)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.get(value)
            if not empl:
                return "Oops! There is no such employee!"
            room = Rooms.query.get(value2)
            if not room:
                return "Oops! There is no such room!"
            if room not in empl.rooms:
                return "Oops! There is no such room for this employee"
            empl.rooms.remove(room)
            db.session.commit()
            return "Successfully removed!"

        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.get(value)
            if not empl:
                return "Oops! There is no such employee!"
            db.session.delete(empl)
            db.session.commit()
            return "Successfully removed!"
        return "Please choose the employee!"
