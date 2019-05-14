from flask import jsonify
from infra.to_dict import to_dict, to_dict_list

def to_result(data, code, message = '', more = ''):
    dados = {
        "result" : {
            "message": message,
            "code": code,
            "more": more
        },
        "data": data
    }
    return dados
