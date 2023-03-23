from datetime import date
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, IntegerField, RadioField, StringField, SubmitField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Regexp


class CryptoForm(FlaskForm):
    id = IntegerField(default = 0, widget=HiddenInput())
    monedaFrom = StringField('Moneda origen', validators=[DataRequired(message='Campo obligatorio.')])
    cantidadFrom = FloatField('Cantidad a invertir', validators=[DataRequired(message='Campo obligatorio.')])
    monedaTo = StringField('Moneda destino', validators=[DataRequired(message='Campo obligatorio.')])

    botonCalcular = SubmitField('Calcular')
    botonEnviar = SubmitField('Enviar')