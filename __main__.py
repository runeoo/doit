from flask import Flask, jsonify, request
from authentication_api import auth_app

from infra.to_dict import to_dict, to_dict_list

app = Flask(__name__)
app.register_blueprint(auth_app)

@app.route('/')
def all():
    
    database = {}
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    