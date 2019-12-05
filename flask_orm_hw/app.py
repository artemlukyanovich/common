from api.rooms import api_bp as rooms_bp
from api.staff import api_bp as staff_bp
from api.tenants import api_bp as tenants_bp

from flask import Flask
from config import get_config
from db import db, migrate, employee_1, employee_2, room_1, room_2, room_3, tenant_1, tenant_2, room_4


def create_app(env="DEFAULT"):
    app = Flask(__name__)
    app.config.from_object(get_config(env))

    app.register_blueprint(rooms_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(tenants_bp)

    db.init_app(app)
    db.drop_all(app=app)

    migrate.init_app(app, db)

    with app.app_context():  # Error while trying to add without "context"
        db.create_all()
        db.session.add(employee_1)
        db.session.add(employee_2)
        db.session.add(room_1)
        db.session.add(room_2)
        db.session.add(room_3)
        db.session.add(room_4)
        employee_1.rooms.append(room_1)
        db.session.add(tenant_1)
        db.session.add(tenant_2)
        db.session.commit()

    return app

