"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import array
import os
from random import randint
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/prueba', methods=['POST'])
def prueba():
    body = request.json  # lo que viene del request como un dic de python 🦎
    try:
        body['last_name'] = (body['last_name'] if 'last_name' in body else "Jackson")
        # response_body = {
        #         "id": body['id'] if body['id'] is not None else jackson_family._generateId(),
        #         "first_name": body['first_name'],
        #         "age": (str(body['age']) if body['age'] is not None else str(randint(0,90))) + " Years old",
        #         "last_name": (body['last_name'] if body['last_name'] is not None else "Jackson"),
        #         "lucky_numbers": body['lucky_numbers'] if body['lucky_numbers'] is not None else list(array.array('i',(randint(0,90) for i in range(0,randint(1,3)))))
        # }
        return jsonify(body), 200
    except Exception as err:
        return jsonify({"message": "Ah ocurrido un error inesperado ‼️" + str(err)}), 500

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_memberbyid(member_id):
    # body = request.json #lo que viene del request como un dic de python 🦎
    try:
        member = jackson_family.get_member(member_id)
        response_body = {
            "family": member
        }
        return jsonify(response_body), 200
    except Exception as err:
        return jsonify({"message": "Ah ocurrido un error inesperado ‼️" + str(err)}), 500

@app.route('/member', methods=['POST'])
def new_member():
    body = request.json  # lo que viene del request como un dic de python 🦎
    try:
        nuevo_member = {
                "id": body['id'] if 'id' in body else jackson_family._generateId(),
                "first_name": body['first_name'],
                "age": (str(body['age']) if 'age' in body else str(randint(0,90))) + " Years old",
                "last_name": (body['last_name'] if 'last_name' in body else "Jackson"),
                "lucky_numbers": body['lucky_numbers'] if 'lucky_numbers' in body else list(array.array('i',(randint(0,90) for i in range(0,randint(1,3)))))
            }
        members = jackson_family.add_member(nuevo_member)
        response_body = {
            "family": members
        }
        return jsonify(response_body), 200
    except Exception as err:
        return jsonify({"message": "Ah ocurrido un error inesperado ‼️" + str(err)}), 500

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # body = request.json  # lo que viene del request como un dic de python 🦎
    try:
        members = jackson_family.delete_member(member_id)
        response_body = {
            "done": True
        }
        return jsonify(response_body), 200
    except Exception as err:
        return jsonify({"message": "Ah ocurrido un error inesperado ‼️" + str(err)}), 500

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
