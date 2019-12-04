import json
from flask import request
from flask_restful import Resource, fields, marshal_with
from db import Staff, db, Rooms, staff_rooms

staff_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}


class StaffRes(Resource):
    def get(self, value=None):
        @marshal_with(staff_structure)  # show() function to make messages correct
        def show(x):
            return x
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            result = Staff.query.filter_by(passport_id=value)
            if not result.count():
                return "Oops! There is no such employee!"
            return show(result.all())
        return show(Staff.query.all())

    def post(self, value=None):
        data = json.loads(request.data)

        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.filter_by(passport_id=value)
            if not empl.count():
                return "Oops! There is no such employee!"
            try:
                room_num = int(data.get('room_number'))
            except ValueError:
                return "Just enter the correct room_number!"
            room = Rooms.query.filter_by(number=room_num)
            if not room.count():
                return "Oops! There is no such room!"
            empl = empl.first()
            room = room.first()
            empl.rooms.append(room)
            db.session.commit()
            return "Successfully added!"

        try:
            name = str(data.get('name'))    # too long :(
            passport_id = int(data.get('passport_id'))
            position = str(data.get('position'))
            salary = int(data.get('salary'))
        except ValueError:
            return "Please enter the correct data!"
        if Staff.query.filter_by(passport_id=passport_id).count():
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
            empl_prev = Staff.query.filter_by(passport_id=value)
            if not empl_prev.count():
                return "Oops! There is no such employee!"
            if Staff.query.filter_by(passport_id=passport_id).count():
                return "Oops! This ID is not available!"
            db.session.delete(empl_prev.first())
            empl_new = Staff(**data)
            db.session.add(empl_new)
            db.session.commit()
            return "Successfully updated!"
        return "Please choose the employee!"

    def delete(self, value=None, value2=None):
        if value and value2:
            try:
                value = int(value)
                value2 = int(value2)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.filter_by(passport_id=value)
            if not empl.count():
                return "Oops! There is no such employee!"
            room = Rooms.query.filter_by(number=value2)
            if not room.count():
                return "Oops! There is no such room!"
            empl = empl.first()
            room = room.first()
            empl.rooms.remove(room)
            db.session.commit()
            return "Successfully removed!"

        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.filter_by(passport_id=value)
            if not empl.count():
                return "Oops! There is no such employee!"
            db.session.delete(empl.first())
            db.session.commit()
            return "Successfully removed!"
        return "Please choose the employee!"


