from model.authentication_model import Auth
from infra.log import Log

professores_db = []

class AuthError(Exception):
    pass

def listar():
    return professores_db

def sigin(user, password):
    print("authentication_service -> authentication_model")
    user = Auth(user, password)
    return user.logar()
