from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, SubmitField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired


class CryptoForm(FlaskForm):
    id = IntegerField(default = 0, widget=HiddenInput())
    
    monedaFrom = SelectField('Moneda origen',
                            choices=[('EUR', 'EUR'), ('BTC', 'BTC'), ('ETH', 'ETH'), ('USDT', 'USDT'), ('ADA', 'ADA'),
                                    ('SOL', 'SOL'), ('XRP', 'XRP'), ('DOT', 'DOT'), ('DOGE', 'DOGE'), ('SHIB', 'SHIB')],
                            validators=[DataRequired(message='Campo obligatorio.')])
    
    cantidadFrom = FloatField('Cantidad a invertir', validators=[DataRequired(message='Campo obligatorio.')])

    monedaTo = SelectField('Moneda destino',
                            choices=[('EUR', 'EUR'), ('BTC', 'BTC'), ('ETH', 'ETH'), ('USDT', 'USDT'), ('ADA', 'ADA'),
                                    ('SOL', 'SOL'), ('XRP', 'XRP'), ('DOT', 'DOT'), ('DOGE', 'DOGE'), ('SHIB', 'SHIB')],
                            validators=[DataRequired(message='Campo obligatorio.')])

    botonCalcular = SubmitField('Calcular')
    botonEnviar = SubmitField('Aceptar')