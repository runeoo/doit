from model.product_model import Product as ProductModel
from model.database_connection import create_connection as connection
from infra.log import Log

import sqlite3

products_db = []
database = "./db/products.db"

class ProdutoJaExiste(Exception):
    pass

class ProdutoNaoExiste(Exception):
    pass

def listar():
    con = connection(database)
    cursor = con.cursor()
    sql = 'SELECT * FROM products ORDER BY products.id'
    cursor.execute(sql)
    row = cursor.fetchmany(200)
    for (id, name, value) in row:
        if localizar(id, name) == None:
            produto = ProductModel(id, name, value)
            products_db.append(produto)
    cursor.close()
    con.close()

    return products_db

def localizar(id, name = ''):
    for product in products_db:
        if product.id == id or product.name == name:
            return product
    return None

def criar(name, value):
    log = Log(None)
    con = connection(database)
    cursor = con.cursor()
    sql = "INSERT INTO products (name, value) VALUES (?, ?)"
    cursor.execute(sql, (name, value))
    id = cursor.lastrowid
    if localizar(id, name) != None:
        raise ProdutoJaExiste()

    con.commit()
    cursor.close()
    con.close()
    
    criado = ProductModel(id, name, value)
    products_db.append(criado)
    log.finalizar(criado)
    return criado

def remove(id):
    if localizar(id) != None:
        raise ProdutoNaoExiste()
    log = Log(None)
    con = connection(database)
    cursor = con.cursor()
    sql = "DELETE FROM products WHERE id = (?)"
    cursor.execute(sql, (id,))
    con.commit()
    result = cursor.rowcount
    cursor.close()
    con.close()
    return result

def atualizar(id, name, value):
    return ''