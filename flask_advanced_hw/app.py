import os

from flask import Flask, render_template

from blueprint.supermarkets.main import supermarkets
from blueprint.products.main import products

# app = Flask(__name__)


# def setup_db():
# DB["products"] = []


def create_app():
    # setup_db()
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        app.config['SECRET_KEY'] = os.urandom(15).hex()
        app.register_blueprint(products)
        app.register_blueprint(supermarkets)
        return app


app = create_app()


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
