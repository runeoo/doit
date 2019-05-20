from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from infra.result import to_result
from services.cart_service import \
    finalizar as service_finalizar, \
    Erro


cart_app = Blueprint('cart_app', __name__, template_folder='templates')
products_bd = []

import requests as Req

campos = ["idProduto", "cep", "numero", "complemento"]
tipos = [int, str, int, str]

@cart_app.route('/checkout', methods=['POST'])
def res():
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return jsonify(to_dict(to_result('Campos com o formatos inválidos', 422))), 422
    try:
        criado = service_finalizar(**dados)
        return jsonify(to_result(to_dict(criado), 200, 'Enviado com sucesso!'))
    except Erro:
        return jsonify(to_dict(to_result('Algum erro ocorreu', 409))), 409