import requests
import sqlite3
import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price
    except requests.RequestException:
        print("Error al obtener el precio de Bitcoin")
        return None

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moneda TEXT NOT NULL,
            precio FLOAT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

def insertar_datos(conn, moneda, precio):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bitcoin (moneda, precio) VALUES (?, ?)
    ''', (moneda, precio))
    conn.commit()


conn = sqlite3.connect('cryptos.db')
crear_tabla(conn)

precio_bitcoin = obtener_precio_bitcoin()
if precio_bitcoin is not None:
    insertar_datos(conn, 'USD', precio_bitcoin)
    insertar_datos(conn, 'GBP', precio_bitcoin * 0.73)  # Tasa de conversión ficticia
    insertar_datos(conn, 'EUR', precio_bitcoin * 1.17)  # Tasa de conversión ficticia

conn.close()


