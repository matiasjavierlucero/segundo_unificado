from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField


class MarcaForm(FlaskForm):
    nombre = StringField('NOMBRE',
        render_kw={
        "class":"form-control",
        "placeholder":"Nombre"
    })
    submit = SubmitField('Guardar', render_kw={"class":"btn btn-success"})
