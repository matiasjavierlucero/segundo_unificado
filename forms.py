from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField


class MarcaForm(FlaskForm):
    nombre = StringField('NOMBRE')
    submit = SubmitField('Guardar')
