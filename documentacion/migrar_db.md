### Inicializa el repositorio de migraciones ejecutando el siguiente comando en tu terminal dentro del directorio del proyecto:

```bash
flask db init
```
- Genera una migración inicial para crear las tablas en la base de datos
    - Solo ejecutarlo una vez

```
flask db migrate -m "Initial migration."
```
- Aplica la migración a la base de datos

```
flask db upgrade
```
- Actualiza la base de datos
