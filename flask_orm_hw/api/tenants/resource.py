import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from db import db, Tenants, Rooms

rooms_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "price": fields.Integer
}

tenants_structure1 = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "city": fields.String,
    "street": fields.String
}

tenants_structure2 = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "city": fields.String,
    "street": fields.String,
    "rooms": fields.Nested(rooms_structure)
}

sex_list = ['man', 'woman']


class TenantsRes(Resource):
    def get(self, value=None):
        @marshal_with(tenants_structure1)  # show() function to make messages correct
        def show1(x):
            return x

        @marshal_with(tenants_structure2)
        def show2(x):
            return x
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            result = Tenants.query.get(value)
            if not result:
                return "Oops! There is no such tenant!"
            return show2(result)
        return show1(Tenants.query.all())

    def post(self):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
            passport_id = int(data.get('passport_id'))
            age = int(data.get('age'))
            sex = str(data.get('sex'))
            city = str(data.get('city'))
            street = str(data.get('street'))
            # room_number = int(data.get('room_number'))
        except ValueError:
            return "Please enter the correct data!"
        if Tenants.query.get(passport_id):
            return "Oops! Such tenant already exists!"
        if sex not in sex_list:
            return "Is it man or woman?"

        # for ten in tenants_list:
        #     if ten.room_number == room_number:
        #         return "Oops! This room is already reserved!"
        # for room in rooms_list:
        #     if room.number == room_number:
        #         break
        # else:
        #     return "Oops! There is no such room!"

        ten = Tenants(**data)
        db.session.add(ten)
        db.session.commit()
        # for room in rooms_list:
        #     if room.number == room_number:
        #         room.status = "Not available"
        return "Successfully added!"

    def patch(self, value=None):
        data = json.loads(request.data)
        try:
            name = str(data.get('name'))
            passport_id = int(data.get('passport_id'))
            age = int(data.get('age'))
            sex = str(data.get('sex'))
            city = str(data.get('city'))
            street = str(data.get('street'))
            # room_number = int(data.get('room_number'))
        except ValueError:
            return "Please enter the correct data!"
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"

            # for ten in tenants_list:
            #     if ten.passport_id == value:
            #         pr_room = ten.room_number
            #         tenants_list.remove(ten)
            #         for room in rooms_list:
            #             if room.number == pr_room:
            #                 room.status = "Available"
            #         tenants_list.append(Tenant(name, passport_id, age, sex, city, street, room_number))
            #         for room in rooms_list:
            #             if room.number == room_number:
            #                 room.status = "Not available"

            ten_prev = Tenants.query.get(value)
            if not ten_prev:
                return "Oops! There is no such tenant!"
            if Tenants.query.get(passport_id):
                return "Oops! This ID is not available!"
            if sex not in sex_list:
                return "Is it man or woman?"
            db.session.delete(ten_prev)
            ten_new = Tenants(**data)
            db.session.add(ten_new)
            db.session.commit()
            return "Successfully updated!"
        return "Please choose the tenant!"

    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            # for ten in tenants_list:
            #     if ten.passport_id == value:
            #         pr_room = ten.room_number
            #         tenants_list.remove(ten)
            #         for room in rooms_list:
            #             if room.number == pr_room:
            #                 room.status = "Available"
            ten = Tenants.query.get(value)
            if ten:
                db.session.delete(ten)
                db.session.commit()
                return "Successfully removed!"
            return "Oops! There is no such tenant!"
        return "Please choose the tenant!"

