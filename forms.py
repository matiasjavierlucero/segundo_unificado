from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired

class MarcaForm(FlaskForm):
    nombre = StringField(
        'Nombre',
        validators=[Length(min=3, max=40), DataRequired()],
        render_kw={"class":"form-control", "placeholder":"Nombre"}
    )
    submit = SubmitField(
        'Guardar',
        render_kw={"class":"form-control btn btn-success"}
    )

