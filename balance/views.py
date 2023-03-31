from flask import jsonify, render_template
import requests
from . import app, APIKEY
from .forms import CryptoForm
from .models import APIConnect, DBConnect

RUTA = app.config.get('RUTA')


@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/purchase')
def formulario():
    formulario = CryptoForm()
    return render_template('form.html', form=formulario)

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/api/v1/inversiones')
def mostrar_inversiones():
    try:
        db = DBConnect(RUTA)
        consulta = 'SELECT date, time, monedaFrom, cantidadFrom, monedaTo, cantidadTo FROM Movimientos'
        inversiones = db.consultaSQL(consulta)
        inversiones_con_PU = []
        for inv in inversiones:
            cantidadFrom = inv['cantidadFrom']
            cantidadTo = inv['cantidadTo']
            precioUnitario = cantidadFrom / cantidadTo
            inv['rate'] = precioUnitario
            inversiones_con_PU.append(inv)

        if inversiones_con_PU:
            resultado = {
                'status': 'success',
                'results': inversiones_con_PU
            }
            status_code = 200
        else:
            resultado = {
                'status': 'error',
                'message': 'No hay inversiones en la base de datos'
            }
            status_code = 404

    except:
        resultado = {
            'status': 'error',
            'message': 'Error interno del sistema.'
        }
        status_code = 500
    
    return jsonify(resultado), status_code

@app.route('/api/v1/estado')
def mostrar_estado():
    try:
        db = DBConnect(RUTA)
        consulta = 'SELECT monedaFrom, cantidadFrom, monedaTo, cantidadTo FROM Movimientos'
        inversiones = db.consultaSQL(consulta)

        # Total de € invertidos
        total_euros_invertidos = 0
        euros_atrapados = 0
        for inv in inversiones:
            if inv['monedaFrom'] == 'EUR':
                total_euros_invertidos += inv['cantidadFrom']
            if inv['monedaTo'] == 'EUR':
                euros_atrapados += inv['cantidadTo']
        
        # Saldo de euros invertidos
        saldo_euros_invertidos = euros_atrapados - total_euros_invertidos

        # Valor actual
        cryptos = ['BTC', 'ETH', 'USDT', 'ADA', 'SOL', 'XRP', 'DOT', 'DOGE', 'SHIB']

        valor_actual = 0
        for crypto in cryptos:
            for inv in inversiones:
                suma_cantidadTo = 0
                suma_cantidadFrom = 0
                if inv['monedaTo'] == crypto:
                    suma_cantidadTo += inv['cantidadTo']
                elif inv['monedaFrom'] == crypto:
                    suma_cantidadFrom += inv['cantidadFrom']
                
                total_crypto = suma_cantidadTo - suma_cantidadFrom

                if inv['monedaTo'] == crypto or inv['monedaFrom'] == crypto:
                    conexionAPI = APIConnect()
                    consultar_cambio = conexionAPI.consultar_cambio(crypto, 'EUR')

                cambio = consultar_cambio * total_crypto

                valor_actual += cambio
        
        estados = {}
        estados['total_euros_invertidos'] = total_euros_invertidos
        estados['valor_total_cryptos'] = valor_actual
        estados['valor_actual'] =  saldo_euros_invertidos + total_euros_invertidos + valor_actual
        
        
        # Cryptos en posesión
        
        for crypto in cryptos:
            moneda_obtenida = 0
            moneda_invertida = 0
            for inv in inversiones:
                if inv['monedaTo'] == crypto:
                    moneda_obtenida += inv['cantidadTo']
                if inv['monedaFrom'] == crypto:
                    moneda_invertida += inv['cantidadFrom']
                    
            total_moneda = moneda_obtenida - moneda_invertida
            estados[crypto] = total_moneda



        if estados:
            resultado = {
                'status': 'success',
                'results': estados
            }
            status_code = 200
        else:
            resultado = {
                'status': 'error',
                'message': 'Error'
            }
            status_code = 404
    except:
        resultado = {
            'status': 'error',
            'message': 'Error interno del servidor.'
        }
        status_code = 500

    return jsonify(resultado), status_code

@app.route('/api/v1/invertir', methods=['POST'])
def invertir():
    pass
