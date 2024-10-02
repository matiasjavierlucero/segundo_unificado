
from datetime import timedelta
from flask import Blueprint ,request, jsonify

from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,

)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from app import db
from models import User
from schemas import UserSchema

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/users', methods=['POST', 'GET'])
@jwt_required()
def user():
   
    if request.method == 'POST':
        additional_data = get_jwt()
        administrador = additional_data.get('administrador')
        if administrador is True:
            data = request.get_json()
            username = data.get('nombre_usuario')
            password = data.get('password')

            password_hasheada = generate_password_hash(
                password=password,
                method='pbkdf2',
                salt_length=8,
            )
            try:
                nuevo_usuario = User(
                    username=username,
                    password_hash=password_hasheada
                )
                db.session.add(nuevo_usuario)
                db.session.commit()

                return jsonify({"Usuario Creado": username}), 201
            except:
                return jsonify({"Error": "Algo salio mal"})
        return jsonify(Mensaje="Ud no esta habilitado para crear un usuario")
    
    usuarios = User.query.all()
    return UserSchema().dump(usuarios, many=True)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password = data.password

    usuario = User.query.filter_by(username=username).first()

    if usuario and check_password_hash(
        pwhash=usuario.password_hash, password=password
    ):
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=10),
            additional_claims=dict(
                administador=usuario.is_admin
            )
        )
        return jsonify({"Token": access_token})

    return jsonify({"Mensaje":"NO MATCH"})
