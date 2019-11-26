from flask import Flask, current_app
from flask_restful import Api
from config import run_config
from routes.rooms import api_bp as rooms_bp
from routes.staff import api_bp as staff_bp


app = Flask(__name__)
api = Api(app)
app.config.from_object(run_config())

app.register_blueprint(rooms_bp)
app.register_blueprint(staff_bp)


@app.route("/")
def hello():
    return current_app.config["SECRET_KEY"]


if __name__ == "__main__":
    app.run(debug=True)