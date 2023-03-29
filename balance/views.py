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
        consulta = 'SELECT date, time, monedaFrom, cantidadFrom, monedaTo, cantidadTo FROM Movimientos'
        inversiones = db.consultaSQL(consulta)
        print('0', inversiones)

        total_euros_invertidos = 0
        euros_atrapados = 0
        for inv in inversiones:
            if inv['monedaFrom'] == 'EUR':
                total_euros_invertidos += inv['cantidadFrom']
        for inv in inversiones:
            if inv['monedaTo'] == 'EUR':
                euros_atrapados += inv['cantidadTo']
        
        saldo_euros_invertidos = euros_atrapados - total_euros_invertidos
        estados = {}
        estados['total_euros_invertidos'] = total_euros_invertidos
        estados['saldo_euros_invertidos'] = saldo_euros_invertidos

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

    return jsonify(resultado), status_code