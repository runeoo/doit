from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from services.authentication_service import \
    sigin as service_sigin, \
    AuthError
from infra.to_dict import to_dict, to_dict_list

campos = ["username", "password"]
tipos = [str, str]

auth_app = Blueprint('auth_app', __name__, template_folder='templates')
auth_bd = []

@auth_app.route('/user', methods=['GET'])
def listar():
    return jsonify(auth_bd)

@auth_app.route('/sigin', methods=['POST'])
def sigin():
    body = request.get_json()
    if not validar_campos(body, campos, tipos):
        return '', 422
    try:
        sigin = service_sigin(body['username'], body['password'])
        print(sigin)
        return sigin
    except AuthError:
        return '', 401
