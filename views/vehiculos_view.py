from flask import Blueprint, request, make_response, jsonify
from app import db

from models import Vehiculo, Marca, Tipo
from schemas import MarcaSchema, TipoSchema, VehiculoSchema

vehiculo_bp = Blueprint('vehiculos', __name__)

@vehiculo_bp.route('/marcas', methods=['GET'])
def marcas():
    marcas = Marca.query.all()
    return MarcaSchema().dump(marcas, many=True)

@vehiculo_bp.route('/tipos', methods=['GET'])
def tipos():
    tipos = Tipo.query.all()
    return TipoSchema().dump(tipos, many=True)

@vehiculo_bp.route('/vehiculos', methods=['GET', 'POST'])
def vehiculos():
    if request.method== "POST":
        data = request.get_json()
        errors = VehiculoSchema().validate(data)

        if errors:
            return make_response(jsonify(errors))
        
        nuevo_vehiculo = Vehiculo(
            modelo = data.get('modelo'),
            anio_fabricacion = data.get('anio_fabricacion'),
            precio = data.get('precio'),
            marca_id = data.get('marca_id'),
            tipo_id = data.get('tipo_id')
        )
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        return VehiculoSchema().dump(nuevo_vehiculo)
    vehiculos = Vehiculo.query.all()
    return VehiculoSchema().dump(vehiculos, many=True)

