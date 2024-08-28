from repositories.marca_repository import MarcaRepository


class MarcaService:
    def __init__(
        self, marca_repository: MarcaRepository
    ):
        self._marca_repository = marca_repository

    def get_all(self):
        return self._marca_repository.get_all()
    
    def create(self, nombre):
        marca = self._marca_repository.create(nombre)
        return marca
