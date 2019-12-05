import json
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from db import db, Tenants, Rooms

rooms_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "price": fields.Integer
}

"""Separate structure to make it easier in hw to copy-past and post a new record"""
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
        def show2(x):   # show2() to see the tenant's rooms
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
        ten = Tenants(**data)
        db.session.add(ten)
        db.session.commit()
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
        except ValueError:
            return "Please enter the correct data!"
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            tenant = Tenants.query.get(value)
            if not tenant:
                return "Oops! There is no such tenant!"
            if value != passport_id:
                return "You can't change password ID!"
            if sex not in sex_list:
                return "Is it man or woman?"
            tenant.name = name
            tenant.age = age
            tenant.sex = sex
            tenant.city = city
            tenant.street = street
            db.session.commit()
            return "Successfully updated!"
        return "Please choose the tenant!"

    def delete(self, value=None):
        if value:
            try:
                value = int(value)
            except ValueError:
                return "Please enter the correct data!"
            ten = Tenants.query.get(value)
            if ten:
                db.session.delete(ten)
                db.session.commit()
                return "Successfully removed!"
            return "Oops! There is no such tenant!"
        return "Please choose the tenant!"

