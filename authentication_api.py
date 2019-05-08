from flask import Blueprint, jsonify, request
auth_app = Blueprint('auth_app', __name__, template_folder='templates')
auth_bd = []

@auth_app.route('/user', methods=['GET'])
def listar():
    return jsonify(auth_bd)

