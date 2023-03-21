from flask import render_template
import json
import requests
from . import app, APIKEY
from .models import APIConnect, DBConnect

RUTA = app.config.get('RUTA')


@app.route('/')
def home():
    db = DBConnect(RUTA)
    mostrar_inversiones = db.mostrarInversiones()
    for inv in mostrar_inversiones:
        monedaFrom = inv.get('monedaFrom')
        monedaTo = inv.get('monedaTo')
        conexionApi = APIConnect()
        precioUnitario = conexionApi.consultar_cambio(monedaFrom, monedaTo)
        # inv['precioUnidad'] = precioUnitario
        # precioAñadido = json.dump
    
    return render_template('inicio.html', inv=mostrar_inversiones) #inv=precioAñadido)


@app.route('/purchase')
def formulario():
    return render_template('form.html')

@app.route('/status')
def status():
    return render_template('status.html')