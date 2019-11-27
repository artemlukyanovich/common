import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from routes.rooms.resource import rooms_list


class Tenant:
    def __init__(self, name: str, passport_id: int, age: int, sex: str, city: str, street: str, room_number: int):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = {
            "city": city,
            "street": street
        }
        self.room_number = room_number


tenants_list = list()
tenants_list.append(Tenant("Anna", 22224444, 30, "woman", "Lviv", "Rustavely", 32))
tenants_list.append(Tenant("Boris", 33336666, 58, "man", "Kharkiv", "Svobody", 21))

address_structure = {
    "city": fields.String,
    "street": fields.String
}

tenants_structure = {
    "name": fields.String,
    "passport_id": fields.Integer,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.Nested(address_structure),
    "room_number": fields.Integer
}

sex_list = ['man', 'woman']


class Tenants(Resource):
    def get(self, value=None):
        @marshal_with(tenants_structure)  # show() function to make messages correct
        def show(x):
            return x
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for ten in tenants_list:
                if ten.passport_id == value:
                    return show(ten)
            return "There is no such tenant!"
        return show(tenants_list)

    # def post(self):
    #     return "Sorry, you can't add tenant!"  # specs

    def post(self):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
            passport_id = int(data.get('passport_id'))
            age = int(data.get('age'))
            sex = str(data.get('sex'))
            city = str((data.get('address'))['city'])
            street = str((data.get('address'))['street'])
            room_number = int(data.get('room_number'))
        except ValueError:
            return "Please enter the correct data!"
        if sex not in sex_list:
            return "Is it man or woman?"
        for ten in tenants_list:
            if ten.passport_id == passport_id:
                return "Oops! Such tenant already exists!"
        for ten in tenants_list:
            if ten.room_number == room_number:
                return "Oops! This room is already reserved!"
        for room in rooms_list:
            if room.number == room_number:
                break
        else:
            return "Oops! There is no such room!"
        tenants_list.append(Tenant(name, passport_id, age, sex, city, street, room_number))
        for room in rooms_list:
            if room.number == room_number:
                room.status = "Not available"
        return "Successfully added!"

    def patch(self, value=None):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
            passport_id = int(data.get('passport_id'))
            age = int(data.get('age'))
            sex = str(data.get('sex'))
            city = str((data.get('address'))['city'])
            street = str((data.get('address'))['street'])
            room_number = int(data.get('room_number'))
        except ValueError:
            return "Please enter the correct data!"
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for ten in tenants_list:
                if ten.passport_id == value:
                    pr_room = ten.room_number
                    tenants_list.remove(ten)
                    for room in rooms_list:
                        if room.number == pr_room:
                            room.status = "Available"
                    tenants_list.append(Tenant(name, passport_id, age, sex, city, street, room_number))
                    for room in rooms_list:
                        if room.number == room_number:
                            room.status = "Not available"
                    return "Successfully updated!"
            return "There is no such tenant!"
        return "Please choose the tenant!"

    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            for ten in tenants_list:
                if ten.passport_id == value:
                    pr_room = ten.room_number
                    tenants_list.remove(ten)
                    for room in rooms_list:
                        if room.number == pr_room:
                            room.status = "Available"
                    return "Successfully removed!"
            return "There is no such tenant!"
        return "Please choose the tenant!"


