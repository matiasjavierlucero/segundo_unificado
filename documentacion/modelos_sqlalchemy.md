# Explicación Detallada de los Modelos en Flask-SQLAlchemy

```python
from app import db

# Definición del modelo Marca
class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Campo id de tipo Integer que es la clave primaria
    nombre = db.Column(db.String(50), nullable=False)  # Campo nombre de tipo String con un máximo de 50 caracteres, no puede ser nulo
    
    def __str__(self):
        return self.nombre  # Método para devolver el nombre de la marca como su representación en cadena

# Definición del modelo Tipo
class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Campo id de tipo Integer que es la clave primaria
    nombre = db.Column(db.String(50), nullable=False)  # Campo nombre de tipo String con un máximo de 50 caracteres, no puede ser nulo

# Definición del modelo Vehiculo
class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Campo id de tipo Integer que es la clave primaria
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)  # Campo tipo_id que es una clave foránea referenciando al id en el modelo Tipo, no puede ser nulo
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)  # Campo marca_id que es una clave foránea referenciando al id en el modelo Marca, no puede ser nulo
    modelo = db.Column(db.String(50), nullable=False)  # Campo modelo de tipo String con un máximo de 50 caracteres, no puede ser nulo
    cilindrada = db.Column(db.String(10), nullable=False)  # Campo cilindrada de tipo String con un máximo de 10 caracteres, no puede ser nulo
    precio = db.Column(db.Integer, nullable=False)  # Campo precio de tipo Integer, no puede ser nulo

    # Relación con el modelo Tipo
    tipo = db.relationship('Tipo', backref=db.backref('vehiculos', lazy=True))  
    # La relación especifica que cada vehículo tiene un tipo. 
    # El parámetro backref agrega una relación inversa desde Tipo al modelo Vehiculo, permitiendo acceder a los vehículos desde un tipo específico.
    # El parámetro lazy=True significa que SQLAlchemy cargará los datos relacionados en el momento en que se accedan a ellos.

    # Relación con el modelo Marca
    marca = db.relationship('Marca', backref=db.backref('vehiculos', lazy=True))  
    # La relación especifica que cada vehículo tiene una marca.
    # El parámetro backref agrega una relación inversa desde Marca al modelo Vehiculo, permitiendo acceder a los vehículos desde una marca específica.
    # El parámetro lazy=True significa que SQLAlchemy cargará los datos relacionados en el momento en que se accedan a ellos.
```