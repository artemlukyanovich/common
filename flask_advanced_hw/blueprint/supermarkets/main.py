import json
import os
import uuid

from flask import Blueprint, request, Response, render_template, redirect, jsonify, url_for, session

from werkzeug.utils import secure_filename
from wtforms import StringField, Form, validators, IntegerField, FileField, TextAreaField, FloatField

from infrastructure import DB

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates')


class SMForm(Form):
    name = StringField('name', [validators.DataRequired()], render_kw={"class": "form-control"})
    location = StringField('name', [validators.DataRequired()], render_kw={"class": "form-control"})
    image = FileField('image', render_kw={"class": "form-control", "accept": "image/jpeg,image/png"})


@supermarkets.route('/add_supermarket', methods=["POST", "GET"])
def add_supermarket():
    form = SMForm(request.form)
    if form.validate and request.method == "POST":
        image = request.files['image']
        img_name = secure_filename(image.filename)
        path = os.path.join('static/supermarkets', img_name)
        image.save(path)
        data = {"id": str(uuid.uuid4()), "name": form.name.data, "location": form.location.data,
                "img_name": img_name}
        DB['supermarkets'].append(data)

    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/supermarket', methods=["GET"])
def get_all_supermarkets():
    args = {}
    result = DB['supermarkets']
    if request.args:
        for p in request.args:
            args['name'] = p
            args['val'] = request.args.get(p)
            result = [i for i in DB['supermarkets'] if str(i[p]) == str(request.args.get(p))]
    return render_template("all_supermarkets.html", supermarkets=result, args=args)


@supermarkets.route('/supermarket/<id>', methods=["GET"])
def get_supermarket(id):
    for sm in DB['supermarkets']:
        if sm['id'] == str(id):
            return render_template("supermarket.html", supermarket=sm)
        else:
            return Response(status=404)


# @supermarkets.route('/supermarket', methods=["GET"])
# def get_all_supermarkets():
#     data = json.dumps(DB)
#     return Response(data, status=200)
#
#     # return jsonify(DB), 200

