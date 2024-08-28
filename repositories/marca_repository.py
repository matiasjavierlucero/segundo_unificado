from app import db
from models import Marca

class MarcaRepository:
    """
    Va ser la clase encargada de manejar el modelo en la DB
    """
    def get_all(self):
        return Marca.query.all()

    def create(self, nombre):
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return nueva_marca
