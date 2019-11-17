import json
import os
import uuid

from flask import Blueprint, request, Response, render_template, redirect, jsonify, url_for

from werkzeug.utils import secure_filename
from wtforms import StringField, Form, validators, IntegerField, FileField, TextAreaField, FloatField
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField

from blueprint.products.model import Product
from infrastructure import DB

products = Blueprint('products', __name__, template_folder='templates')


# @products.route('/add_product', methods=['GET', 'POST'])
# def add_product():
#     form = ProductForm(request.form)
#     if request.method == 'POST' and form.validate():
#         img_name = ''
#         if request.files['image']:
#             image = request.files['image_src']
#             img_name = secure_filename(image.filename)
#             path = os.path.join('static', img_name)
#             image.save(path)
#
#         data = {"id": str(uuid.uuid4()), "name": form.name.data, "description": form.description.data,
#                 "img_name": img_name, "price": form.price.data}
#         DB['products'].append(data)
#
#     return render_template('add_product.html', form=form)


# @products.route('/add_product', methods=['GET', 'POST'])
# def add_product():
#     form = ProductForm()
#     if request.method == 'POST':
#         data = {"id": str(uuid.uuid4()), "name": request.form['name'], "description": request.form['description'],
#                 "img_name": secure_filename(request.files['image_src'].filename), "price": request.form['price']}
#         DB['products'].append(data)
#
#         file = request.files['image_src']
#         filename = secure_filename(file.filename)
#         path = os.path.join('static', filename)
#         file.save(path)
#
#     return render_template('add_product.html', form=form)


class ProductForm(Form):
    name = StringField('name', [validators.DataRequired()], render_kw={"class": "form-control"})
    description = StringField('description', [validators.DataRequired()], render_kw={"class": "form-control"})
    price = IntegerField('price', [validators.DataRequired()], render_kw={"class": "form-control"})
    image = FileField('image', render_kw={"class": "form-control", "accept": "image/jpeg,image/png"})


@products.route('/add_product', methods=["POST", "GET"])
def add_product_save():
    form = ProductForm(request.form)
    if form.validate and request.method == "POST":
        image = request.files['image']
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

