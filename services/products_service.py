from model.product_model import Product as ProductModel
from model.database_connection import create_connection as connection
from infra.log import Log

import sqlite3

database = "./db/products.db"

class ProdutoJaExiste(Exception):
    pass

class ProdutoNaoExiste(Exception):
    pass

def listar():
    products_db = []
    con = connection(database)
    cursor = con.cursor()
    sql = 'SELECT * FROM products ORDER BY products.id'
    cursor.execute(sql)
    row = cursor.fetchmany(200)
    for (id, name, value) in row:
        produto = ProductModel(id, name, value)
        products_db.append(produto)
    cursor.close()
    con.close()

    return products_db

def listar_id(id):
    products_db = []
    con = connection(database)
    cursor = con.cursor()
    sql = 'SELECT * FROM products WHERE id = (?)'
    cursor.execute(sql, (id, ))
    row = cursor.fetchone()
    produto = ProductModel(row[0], row[1], row[2])
    products_db.append(produto)
    cursor.close()
    con.close()

    return products_db


def localizar(id, name = ''):
    products_db = listar()
    for product in products_db:
        if product.id == id or product.name == name:
            return product
    return None


def criar(name, value):
    log = Log(None)
    
    if localizar(0, name) != None:
        raise ProdutoJaExiste()
    con = connection(database)
    cursor = con.cursor()
    sql = 'INSERT INTO products (name, value) VALUES (?, ?)'
    cursor.execute(sql, (name, value))
    row_id = cursor.lastrowid
    con.commit()
    con.close()

    criado = ProductModel(row_id, name, value)
    log.finalizar(criado)

    return criado

def remove(id):
    log = Log(None)

    if localizar(id) == None:
        raise ProdutoNaoExiste()
    
    con = connection(database)
    cursor = con.cursor()
    sql = 'DELETE FROM products WHERE id = ?'
    cursor.execute(sql, (id,))
    result = cursor.rowcount
    con.commit()
    con.close()

    return result

def atualizar(id, name, value):
    return ''