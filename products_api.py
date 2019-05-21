from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from infra.result import to_result
from services.products_service import \
    listar as service_listar, \
    listar_id as service_listar_id, \
    criar as service_criar, \
    remove as service_delete, \
    ProdutoJaExiste, ProdutoNaoExiste

products_app = Blueprint('products_app', __name__, template_folder='templates')
products_bd = []

campos = ["name", "value"]
tipos = [str, float]

@products_app.route('/produtos', methods=['GET', 'POST'])
def listar():
    if request.method == 'GET':
        lista = service_listar()
        return jsonify(to_result(to_dict_list(lista), 200))
    else:
        dados = request.get_json()
        if not validar_campos(dados, campos, tipos):
            return jsonify(to_dict(to_result('Campos com o formato inválido', 422))), 422
        try:
            criado = service_criar(**dados)
            return jsonify(to_result(to_dict(criado), 200, 'Adicionado com sucesso'))
        except ProdutoJaExiste:
            return jsonify(to_dict(to_result('Produto já existe', 400))), 400

@products_app.route('/produtos/<int:id>', methods=['GET'])
def listar_id(id):
    lista = service_listar_id(id)
    return jsonify(to_result(to_dict_list(lista), 200))

@products_app.route('/produtos/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        delete = service_delete(id)
        return jsonify(to_result(to_dict(delete), 200, 'Deletado com sucesso!'))
    except ProdutoNaoExiste:
        return jsonify(to_dict(to_result('Produto não existe', 409))), 409

