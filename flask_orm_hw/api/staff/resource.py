import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from flask_restful import Resource, fields, marshal_with

from db import Staff, db

staff_structure = {
    "name": fields.String,
    "passport_id": fields.Integer,
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

    def post(self):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
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
            if empl_prev.count():
                db.session.delete(empl_prev.first())
                empl_new = Staff(**data)
                db.session.add(empl_new)
                db.session.commit()
                return "Successfully updated!"
            return "Oops! There is no such employee!"
        return "Please choose the employee!"

    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            empl = Staff.query.filter_by(passport_id=value)
            if empl.count():
                db.session.delete(empl.first())
                db.session.commit()
                return "Successfully removed!"
            return "Oops! There is no such employee!"
        return "Please choose the employee!"


