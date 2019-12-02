import json
from flask import render_template, request, Blueprint
from models.item import Dolar

item_blueprint = Blueprint('items', __name__)


@item_blueprint.route('/')
def index():
    items = Dolar.all()
    return render_template('items/index.html', items=items)


@item_blueprint.route('/new', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']

        Dolar(url, tag_name).save_to_mongo()

    return render_template('items/new_item.html')




