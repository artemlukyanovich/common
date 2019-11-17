import json
import os
import uuid

from flask import Blueprint, request, Response, render_template, redirect, jsonify, url_for

from werkzeug.utils import secure_filename
from wtforms import StringField, Form, validators, IntegerField, FileField
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField

from blueprint.products.model import Product
from infrastructure import DB

products = Blueprint('products', __name__, template_folder='templates')


class ProductForm(Form):
    name = StringField('name', validators=[validators.input_required()])
    description = StringField('description', validators=[validators.input_required()])
    price = IntegerField('price', validators=[validators.input_required()])
    image_src = FileField('image_src', validators=[validators.input_required()])


@products.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        image = request.files['image_src']
        img_name = secure_filename(image.filename)
        path = os.path.join('static', img_name)
        image.save(path)

        data = {"id": str(uuid.uuid4()), "name": form.name.data, "description": form.description.data,
                "img_name": img_name, "price": form.price.data}
        DB['products'].append(data)

    return render_template('add_product.html', form=form)


@products.route('/product', methods=['GET'])
def all_products():
    # data = json.dumps(DB)
    # return Response(data, status=200)

    return jsonify(DB), 200

