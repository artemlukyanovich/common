from flask import Flask, render_template

from infrastructure import DB
from blueprint.products.main import products

# app = Flask(__name__)


# def setup_db():
#     DB["products"] = []


def create_app():
    # setup_db()
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        app.register_blueprint(products)
        return app


app = create_app()

# app.register_blueprint(products)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
