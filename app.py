import os

from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuracion de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/repaso_flask_primer_semestre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Tipo, Vehiculo
from forms import MarcaForm
from services.marca_service import MarcaService
from repositories.marca_repository import MarcaRepository

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/marca_list", methods=['POST', 'GET'])
def marcas():   
    marca_service = MarcaService(MarcaRepository())
    marcas = marca_service.get_all()

    formulario = MarcaForm()

    if request.method == 'POST':
        nombre=formulario.nombre.data
        marca_service.create(nombre)
        return redirect(url_for('marcas'))

    return render_template(
        'marca_list.html',
        marcas=marcas, 
        formulario=formulario,
    )

@app.route("/marca/<id>/vehiculos")
def vehiculos_por_marca(id):
    #vehiculos = Vehiculo.query.filter_by(marca_id=id)
    marca = Marca.query.get_or_404(id)
    vehiculos = marca.vehiculos
    return render_template(
        "vehiculos_by_marca.html",
        vehiculos=vehiculos,
        marca=marca
    )

@app.route("/marca/<id>/editar", methods=['GET', 'POST'])
def marca_editar(id):
    marca = Marca.query.get_or_404(id)

    if request.method == 'POST':
        marca.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('marcas'))

    return render_template(
        "marca_edit.html",
        marca=marca
    )

@app.route("/tipo_list")
def tipos():
    tipos = Tipo.query.all()
    return render_template('tipo_list.html', tipos=tipos)


@app.route("/vehiculos_list", methods = ['POST', 'GET'])
def vehiculos():
    vehiculos = Vehiculo.query.all()
    marcas = Marca.query.all()
    tipos = Tipo.query.all()

    if request.method == 'POST':
        modelo = request.form['modelo']
        anio = request.form['anio_fabricacion']
        precio = request.form['precio']
        marca = request.form['marca']
        tipo = request.form['tipo']
        vehiculo_nuevo = Vehiculo(
            modelo=modelo,
            anio_fabricacion=anio,
            precio=precio,
            marca_id=marca,
            tipo_id=tipo,
        )
        db.session.add(vehiculo_nuevo)
        db.session.commit()
        return redirect(url_for('vehiculos'))

    return render_template(
        'vehiculos_list.html',
        vehiculos=vehiculos,
        marcas=marcas,
        tipos=tipos,
    )
