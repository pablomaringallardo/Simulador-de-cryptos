import requests
import sqlite3
from . import APIKEY

class APIError(Exception):
    pass

class APIConnect:

    def __init__(self):
        self.apiurl = 'http://rest.coinapi.io'
        headers = {
            'X-CoinAPI-Key': APIKEY
        }
        self.headers = headers
        self.cambio = 0.0

    def consultar_cambio(self, origen, destino):
        endpoint = f'/v1/exchangerate/{origen}/{destino}'
        url = self.apiurl + endpoint
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            exchange = response.json()
            self.cambio = exchange.get('rate')
            return self.cambio
        else:
            raise APIError(
                f'Error {response.status_code} {response.reason} al consultar la API'
            )

class DBConnect:

    def __init__(self, ruta):
        self.ruta = ruta
    
    def mostrarInversiones(self):
        consulta = 'SELECT date, time, monedaFrom, cantidadFrom, monedaTo, cantidadTo FROM Movimientos'
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)
        datos = cursor.fetchall()

        self.inversiones = []
        nombres_columna = []
        for columna in cursor.description:
            nombres_columna.append(columna[0])

        for dato in datos:
            indice = 0
            inversion = {}
            for nombre in nombres_columna:
                inversion[nombre] = dato[indice]
                indice += 1

            self.inversiones.append(inversion)
        
        conexion.close()

        return self.inversiones

