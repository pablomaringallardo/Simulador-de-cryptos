from flask import Flask


APIKEY = '02A1D6CB-9364-4D1E-89F7-4E15A69713B0'


app = Flask(__name__)
app.config.from_object('config')