import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse


class Employee:
    def __init__(self, name: str, passport_id: int, position: str, salary: int):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff_list = list()
staff_list.append(Employee("Ivan", 12345678, "Manager", 500))
staff_list.append(Employee("Vania", 87654321, "Cleaner", 20))

staff_structure = {
    "name": fields.String,
    "passport_id": fields.Integer,
    "position": fields.String,
    "salary": fields.Integer
}


class Staff(Resource):
    def get(self, value=None):
        @marshal_with(staff_structure)  # show() function to make messages correct
        def show(x):
            return x
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for empl in staff_list:
                if empl.passport_id == value:
                    return show(empl)
            return "There is no such employee!"
        return show(staff_list)

    # def post(self):
    #     return "Sorry, you can't add employee!"

    def post(self):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
            passport_id = int(data.get('passport_id'))
            position = str(data.get('position'))
            salary = int(data.get('salary'))
        except ValueError:
            return "Please enter the correct data!"
        for empl in staff_list:
            if empl.passport_id == passport_id:
                return "Oops! Such employee already exists!"
            staff_list.append(Employee(name, passport_id, position, salary))
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
            for empl in staff_list:
                if empl.passport_id == value:
                    staff_list.remove(empl)
                    staff_list.append(Employee(name, passport_id, position, salary))
                    return "Successfully updated!"
            return "There is no such employee!"
        return "Please choose the employee!"

    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for empl in staff_list:
                if empl.passport_id == value:
                    staff_list.remove(empl)
                    return "Successfully removed!"
            return "There is no such employee!"
        return "Please choose the employee!"


