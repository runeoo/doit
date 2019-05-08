class Auth():
    def __init__(self, user, password):
        print('Objeto Auth instanciado.')
        self._user = user
        self._password = password

    def logar(self):
        print('Self chamando logar')
        return self