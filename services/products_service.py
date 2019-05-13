from model.product_model import Product as ProductModel
from infra.log import Log

import sqlite3

products_db = []

class ProdutoJaExiste(Exception):
    pass

class ProdutoNaoExiste(Exception):
    pass

def listar():
    connection = sqlite3.connect("./db/products.db")
    cursor = connection.cursor()
    sql = 'SELECT * FROM products'
    cursor.execute(sql)
    row = cursor.fetchmany(200)
    
    for (id, name, value) in row:
        if localizar(id, name) == None:
            criar(id, name, value)
    cursor.close()
    connection.close()

    return products_db

def localizar(id, name):
    for product in products_db:
        if product.id == id and product.name == name:
            return product
    return None

def criar(id, name, value):
    if localizar(id, name) != None:
        raise ProdutoJaExiste()
    log = Log(None)
    criado = ProductModel(id, name, value)
    products_db.append(criado)
    log.finalizar(criado)
    return criado