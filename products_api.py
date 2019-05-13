from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from infra.result import to_result
from services.products_service import \
    listar as service_listar, \
    criar as service_criar, \
    ProdutoJaExiste

products_app = Blueprint('products_app', __name__, template_folder='templates')
products_bd = []

campos = ["id", "name", "value"]
tipos = [int, str, float]

@products_app.route('/produtos', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_result(to_dict_list(lista), 200))

@products_app.route('/produtos', methods=['POST'])
def criar():
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return jsonify(to_dict(to_result('Campos com o formato inválido', 422))), 422
    try:
        criado = service_criar(**dados)
        return jsonify(to_dict(criado))
    except ProdutoJaExiste:
        return jsonify(to_dict(to_result('Produto já existe', 409))), 409