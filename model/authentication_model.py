from flask import  jsonify
class Auth():
    def __init__(self, user, password):
        print('Objeto Auth instanciado.')
        self._user = user
        self._password = password

    def logar(self):
        users = [
            {"username": "bruno", "pwd": "123"},
            {"username": "bruno2", "pwd": "123"},
            {"username": "bruno4", "pwd": "123"},
        ]
        for user in users:
            if user['username'] == self._user and user["pwd"] == self._password:
                return jsonify({ "token": 12412512 })
            return "Não encontramos nada", 404
