from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)

# можно без db: python manage.py runserver

if __name__ == "__main__":
    manager.run()