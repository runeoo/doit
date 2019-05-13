from flask import Flask, jsonify, request
from products_api import products_app
from infra.to_dict import to_dict, to_dict_list

app = Flask(__name__)
app.register_blueprint(products_app)

@app.route('/')
def all():
    from services.products_service import listar as produtos_listar
    database = {
        "PRODUTOS": to_dict_list(produtos_listar()),
    }
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    