from flask import jsonify
from infra.to_dict import to_dict, to_dict_list

def to_result(data, code):
    dados = {
        "result" : {
            "message": '',
            "code": code,
            "more": ''
        },
        "data": data
    }
    return dados
