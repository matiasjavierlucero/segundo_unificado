from datetime import date

from app import ma

from models import User, Marca, Tipo, Vehiculo
from marshmallow import validates, ValidationError


class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class MinimalUserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User

    username = ma.auto_field()

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca
        
    id = ma.auto_field()
    nombre = ma.auto_field()

class TipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo
        
    id = ma.auto_field()
    nombre = ma.auto_field()

class VehiculoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Vehiculo

    id = ma.auto_field() 
    modelo = ma.auto_field()
    anio_fabricacion = ma.auto_field()
    precio = ma.auto_field()
    marca_id = ma.auto_field()
    tipo_id = ma.auto_field()
    #marca = ma.Nested(MarcaSchema) 
    #tipo = ma.Nested(TipoSchema)

    @validates('anio_fabricacion')
    def validate_anio_fabricacion(self, value):
        if value > 2024:
            raise ValidationError("El año no puede mayor al actual")
        return value

    @validates('precio')
    def validate_precio(self, value):
        if value <= 0:
            raise ValidationError("El precio no es correcto")
        return value
