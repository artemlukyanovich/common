from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


employee_room = db.Table(
    'employee_room',
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.passport_id')),
    db.Column('room_number', db.Integer, db.ForeignKey('room.number'))
)


class Employee(db.Model):
    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    salary = db.Column(db.Integer)
    rooms = db.relationship('Room', secondary=employee_room, backref='staff')


class Room(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.passport_id'))
    # staff = db.relationship('Employee', secondary=employee_room, backref='rooms')


class Tenant(db.Model):
    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    city = db.Column(db.String)
    street = db.Column(db.String)
    rooms = db.relationship('Room', backref='tenant')


employee_1 = Employee(passport_id=12345678, name='Ivan', position='manager', salary=400)
employee_2 = Employee(passport_id=87654321, name='John', position='cleaner', salary=100)

