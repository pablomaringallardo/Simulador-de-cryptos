from . import app

@app.route('/')
def inicio():
    return 'Hola.'

@app.route('/purchase')
def formulario():
    return 'Formulario compra, venta o intercambio.'

@app.route('/status')
def status():
    return 'Estado de la inversion'