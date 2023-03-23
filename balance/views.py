from flask import jsonify, render_template
import requests
from . import app, APIKEY
from .models import APIConnect, DBConnect

RUTA = app.config.get('RUTA')


@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/purchase')
def formulario():
    return render_template('form.html')

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/api/v1/inversiones')
def mostrar_inversiones():
    try:
        db = DBConnect(RUTA)
        consulta = 'SELECT date, time, monedaFrom, cantidadFrom, monedaTo, cantidadTo FROM Movimientos'
        inversiones = db.consultaSQL(consulta)
        print('1', inversiones)
        inversiones_con_PU = []
        for inv in inversiones:
            cantidadFrom = inv['cantidadFrom']
            cantidadTo = inv['cantidadTo']
            precioUnitario = cantidadFrom / cantidadTo
            print('4', precioUnitario)
            inv['rate'] = precioUnitario
            print(inv)
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