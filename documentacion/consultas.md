
## Consultar Objetos

### Listar todos los Vehículos

Para obtener todos los objetos de un modelo, utilizamos el método `query.all()`:

```python
vehiculos = Vehiculo.query.all()
# Esto devuelve una lista de todos los vehículos en la base de datos.
```

### Obtener un Vehículo por ID

Para obtener un objeto por su ID, utilizamos el método `query.get_or_404(id)`:

```python
vehiculo = Vehiculo.query.get_or_404(1)
# Esto devuelve el vehículo con el ID 1. Si no se encuentra, lanza un error 404.
```

### Obtener Vehículos por Marca

Para obtener todos los vehículos de una marca específica utilizando la relación definida en el modelo:

```python
marca = Marca.query.get_or_404(1)
vehiculos = marca.vehiculos
# Esto devuelve una lista de todos los vehículos que pertenecen a la marca con el ID 1.
```

## Crear Objetos

Para crear un nuevo objeto, se utiliza el método `db.session.add()` seguido de `db.session.commit()`:

```python
nueva_marca = Marca(nombre="Tesla")
db.session.add(nueva_marca)
db.session.commit()
# Esto crea una nueva marca llamada "Tesla" y la guarda en la base de datos.
```

## Editar Objetos

Para editar un objeto existente, primero se obtiene el objeto, se actualizan sus campos y luego se guarda:

```python
marca = Marca.query.get_or_404(1)
marca.nombre = "Tesla Actualizado"
db.session.commit()
# Esto actualiza el nombre de la marca con ID 1 a "Tesla Actualizado" y guarda los cambios en la base de datos.
```

## Eliminar Objetos

Para eliminar un objeto, primero se obtiene el objeto y luego se elimina utilizando el método `db.session.delete()` seguido de `db.session.commit()`:

```python
vehiculo = Vehiculo.query.get_or_404(1)
db.session.delete(vehiculo)
db.session.commit()
# Esto elimina el vehículo con ID 1 de la base de datos.
```