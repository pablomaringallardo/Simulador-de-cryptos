from . import app

@app.route('/')
def inicio():
    return (f'La ruta del archivo de datos es: {app.config["RUTA"]}<br>'
            f'Secret key: {app.config["SECRET_KEY"]}')


@app.route('/purchase')
def formulario():
    return 'Formulario compra, venta o intercambio.'

@app.route('/status')
def status():
    return 'Estado de la inversion'