from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def all():
    
    database = {}
    return jsonify(database)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
