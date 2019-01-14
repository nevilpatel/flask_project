import random

from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)

catalog = [
    {
        'name': 'Daal',
        'vendor': 'Vendor1',
        'category': 'Veg',
        'item_id': 1
    },
    {
        'name': 'Bhaat',
        'vendor': 'Vendor1',
        'category': 'Veg',
        'item_id': 2
    },
    {
        'name': 'Chicken-Tikka',
        'vendor': 'Vendor2',
        'category': 'Non-Veg',
        'item_id': 3
    }
]


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


def replaced_response():
    return create_response(status=204)


def deleted_response():
    return create_response(status=204)


def resource_added_response(location):
    return create_response(status=201, location=location)


# GET
@app.route('/catalog')
def get_catalog():
    return jsonify({'catalog': catalog})


# ADD/POST
@app.route('/catalog', methods=['POST'])
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
    item = {}
    if validate_item(request_data):
        item = {
            'name': request_data['name'],
            'vendor': request_data['vendor'],
            'category': request_data['category'],
            'item_id': random.randint(1, 5000)
        }
        catalog.append(item)
        return resource_added_response('/item/' + str(item['item_id']))
    return invalid_request_response()


# PUT(REPLACE)/catalog/id
# {
#     'name':'new name',
#     'vendor':'new_vendor'
#     'category':'new_category'
# }
@app.route('/catalog/<int:item_id>', methods=['PUT'])
def repalce_item(item_id):
    request_data = request.get_json()
    if validate_item(request_data):
        new_item = {
            'name': request_data['name'],
            'vendor': request_data['vendor'],
            'category': request_data['category'],
            'item_id': item_id
        }
        i = 0
        for item in catalog:
            if item['item_id'] == item_id:
                catalog[i] = new_item
                return replaced_response()
            i += 1
    return resource_not_found_response()


# UPDATE
@app.route('/catalog/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    request_data = request.get_json()
    updated_item = {}
    if "name" in request_data:
        updated_item['name'] = request_data['name']
    if "vendor" in request_data:
        for item in catalog:
            if item['item_id'] == item_id:
                item.update(updated_item)
                return replaced_response()
    return resource_not_found_response()


# DELETE
@app.route('/catalog/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    i = 0
    for item in catalog:
        if item['item_id'] == item_id:
            catalog.pop(i)
            return deleted_response()
        i += 1
    return resource_not_found_response()


@app.route('/item/<int:item_id>')
def get_item(item_id):
    return_value = {}
    for item in catalog:
        if item['item_id'] == id:
            return_value['name'] = item['name']
            return_value['vendor'] = item['vendor']
            return_value['category'] = item['category']
    return jsonify(return_value)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
