import os
import uuid

from flask import Blueprint, request, Response, render_template, redirect, jsonify, url_for, session

from werkzeug.utils import secure_filename
from wtforms import StringField, Form, validators, IntegerField, FileField, TextAreaField, FloatField

from infrastructure import DB

products = Blueprint('products', __name__, template_folder='templates')


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


@products.route('/product', methods=["GET"])
def get_all_products():
    # data_products = DB['products']
    # result = []
    args = {}
    if request.args:
        for param in request.args:
            args['name'] = param
            args['val'] = request.args.get(param)
            result = [i for i in DB['products'] if str(i[param]) == str(request.args.get(param))]
    else:
        result = DB['products']
    return render_template("all_products.html", products=result, args=args)


@products.route('/product/<id>', methods=["GET"])
def get_product(id):
    for p in DB['products']:
        if p['id'] == str(id):
            return render_template("product.html", product=p)
        else:
            return Response(status=404)


# @products.route('/product', methods=["GET"])
# def get_all_products():
#     data = json.dumps(DB)
#     return Response(data, status=200)
#
#     # return jsonify(DB), 200