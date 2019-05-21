from model.product_model import Product as ProductModel
from model.database_connection import create_connection as connection
from infra.log import Log
from services.products_service import \
    listar as service_listar, \
    localizar as service_localizar

import sqlite3
import requests as Req

database = "./db/products.db"

class ProdutoNaoLocalizadoErro(Exception):
    pass


def finalizar(idProduto, cep, numero, complemento):
    cart_db = []
    produto = service_localizar(idProduto)
    if produto == None:
        raise ProdutoNaoLocalizadoErro()

    cart_db.append({"produto": produto})
    url = f"http://viacep.com.br/ws/{cep}/json" 
    retorno = Req.get(url).json()
    retorno["numero"] = numero
    retorno["complemento"] = complemento if complemento else retorno['complemento']
    cart_db.append({"endereco": retorno})
    return cart_db