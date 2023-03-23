from datetime import date
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, IntegerField, RadioField, StringField, SubmitField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Regexp