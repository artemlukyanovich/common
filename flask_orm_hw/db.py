from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


staff_rooms = db.Table(
    'staff_rooms',
    db.Column('employee_id', db.Integer, db.ForeignKey('staff.passport_id')),
    db.Column('room_number', db.Integer, db.ForeignKey('rooms.number'))
)


class Staff(db.Model):
    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    salary = db.Column(db.Integer)
    rooms = db.relationship('Rooms', secondary=staff_rooms, backref='staff')


class Rooms(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.passport_id'))
    # staff = db.relationship('Staff', secondary=staff_rooms, backref='rooms')


class Tenants(db.Model):
    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    city = db.Column(db.String)
    street = db.Column(db.String)
    rooms = db.relationship('Rooms', backref='tenant')


employee_1 = Staff(passport_id=12345678, name='Ivan', position='manager', salary=400)
employee_2 = Staff(passport_id=87654321, name='John', position='cleaner', salary=100)

