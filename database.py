import sqlite3

CREATE_CURRENCY_TABLE = "CREATE TABLE iF NOT EXISTS currency(id INTEGER PRIMARY KEY, name TEXT, type TEXT, circulatingSupply INTEGER, price DECIMAL(27,18));"

INSERT_CURRENCY = "INSERT INTO currency(name, type, circulatingSupply, price) VALUES (?, ?, ?, ?);"

GET_ALL_CURRENCY = "SELECT * FROM currency;"

GET_CURRENCY_BY_NAME = "SELECT * FROM currency WHERE name = ?;"

GET_CURRENCY_BY_PRICE = "SELECT * FROM currency WHERE price <= ?;"

GET_CURRENCY_BY_TYPE = "SELECT * FROM currency WHERE type = ?;"

DELETE_CURRENCY_BY_NAME = "DELETE FROM currency WHERE name = ?;"


def connect():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_CURRENCY_TABLE)

def add_crypto(connection, name, type, circulatingSupply, price):
    with connection: 
        connection.execute(INSERT_CURRENCY, (name, type, circulatingSupply, price))

def get_all_currency(connection):
    with connection:
        return connection.execute(GET_ALL_CURRENCY).fetchall()

def get_currency_by_name(connection, name):
    with connection:
        return connection.execute(GET_CURRENCY_BY_NAME, (name,)).fetchall()

def get_currency_by_price(connection, price):
    with connection:
        return connection.execute(GET_CURRENCY_BY_PRICE, (price,)).fetchall()

def get_currency_by_type(connection, type):
    with connection:
        return connection.execute(GET_CURRENCY_BY_TYPE, (type,)).fetchall()

def delete_currency_by_name(connection, name):
    with connection:
        connection.execute(DELETE_CURRENCY_BY_NAME, (name,))
