from flask import Flask, jsonify, request
from products_api import products_app
from cart_api import cart_app
from infra.to_dict import to_dict, to_dict_list
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(products_app)
app.register_blueprint(cart_app)
CORS(app, supports_credentials=False)

@app.route('/')
def all():
    from services.products_service import listar as produtos_listar
    database = {
        "PRODUTOS": to_dict_list(produtos_listar()),
    }
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
    