import datetime
import random
from functools import wraps

import jwt
from flask import jsonify, request, Response, json

from models.catalog_model import *
from models.user_model import User


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page.'})

    return wrapper


def validate_item(item):
    if 'name' in item and 'vendor' in item and 'category' in item:
        return True
    return False


def get_item_id():
    return random.randint(1, 5000)


def create_response(message="", status=200, location=""):
    response = Response(json.dumps(message), status, mimetype='application/json')
    if location:
        response.headers['LOCATION'] = location
    return response


def resource_not_found_response():
    msgbody = {
        "error": "Resource not found.",
        "helper": "Make sure id passed is correct ......"
    }
    return create_response(msgbody, 404)


def invalid_request_response():
    msgbody = {
        "error": "Invalid request.",
        "helper": "Make sure the body of the request is ......"
    }
    return create_response(msgbody, 400)


def unauthorized_user_response():
    msgbody = {
        "error": "Unauthorized User.",
        "helper": "Username and Password does not match."
    }
    return create_response(msgbody, 401)


def replaced_response():
    return create_response(status=204)


def deleted_response():
    return create_response(status=204)


def resource_added_response(location):
    return create_response(status=201, location=location)


@app.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    if User.user_name_password_match(username, password):
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
        return token
    else:
        return unauthorized_user_response()


# GET
@app.route("/catalog")
def get_catalog():
    return jsonify({'catalog': Catalog.get_catalog()})


# ADD/POST
@app.route('/catalog', methods=['POST'])
@token_required
def add_item():
    """
        POST /catalog
        {
          'name':'Tindora nu shaak',
          'vendor':'Kanzi',
          'category':'Veg',
          'item_id':'6'
        }
    :return: 201
    """
    request_data = request.get_json()
    if validate_item(request_data):
        item_id = get_item_id()
        Catalog.add_item(item_id, request_data['name'], request_data['vendor'], request_data['category'])
        return resource_added_response('/catalog/' + str(item_id))
    return invalid_request_response()


# PUT(REPLACE)/catalog/id
# {
#     'name':'new name',
#     'vendor':'new_vendor'
#     'category':'new_category'
# }
@app.route('/catalog/<int:item_id>', methods=['PUT'])
@token_required
def replace_item(item_id):
    request_data = request.get_json()
    if validate_item(request_data):
        Catalog.replace_item(item_id, request_data['name'], request_data['vendor'], request_data['category'])
        return replaced_response()
    return resource_not_found_response()


# UPDATE
@app.route('/catalog/<int:item_id>', methods=['PATCH'])
@token_required
def update_item(item_id):
    request_data = request.get_json()
    updated = False
    if "name" in request_data:
        Catalog.update_name(item_id, request_data['name'])
        updated = True
    if "vendor" in request_data:
        Catalog.update_vendor(item_id, request_data['vendor'])
        updated = True
    if updated:
        return replaced_response()
    return resource_not_found_response()


# DELETE
@app.route('/catalog/<int:item_id>', methods=['DELETE'])
@token_required
def delete_item(item_id):
    if Catalog.delete_item(item_id):
        return deleted_response()
    return resource_not_found_response()


@app.route('/item/<int:item_id>')
def get_item(item_id):
    return_value = Catalog.get_item(item_id)
    if len(return_value) > 0:
        return jsonify(return_value)
    else:
        return resource_not_found_response()


if __name__ == '__main__':
    app.run(debug=True, port=5001)
