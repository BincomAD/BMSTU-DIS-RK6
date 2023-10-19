from flask import Blueprint, render_template, request
from db.db import getProduct, getByPrice, getByCategory

supermarket = Blueprint('supermarket', __name__)

@supermarket.route('/list', methods=['GET'])
def list():
    results = getProduct()

    return render_template('result.html', results=results)

@supermarket.route('/price', methods=['POST'])
def price():
    ot = int(request.form['ot'])
    do = int(request.form['do'])
    results = getByPrice(ot, do)

    return render_template('result.html', results=results)

@supermarket.route('/category', methods=['POST'])
def category():
    cat = int(request.form['category'])
    results = getByCategory(cat)

    return render_template('result.html', results=results)


