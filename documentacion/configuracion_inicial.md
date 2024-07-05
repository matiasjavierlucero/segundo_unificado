# Guía para Configuración de Flask con Flask-Migrate y MySQL

## Paso 1: Instalación de Librerías Necesarias

Instala Flask, Flask-SQLAlchemy, Flask-Migrate y PyMySQL:

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL
```
```python
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/repaso'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models
```

## Explicación de cada línea:
- ```from flask import Flask, render_template, redirect, request```
    - Importa las funciones necesarias de Flask.

- ```from flask_sqlalchemy import SQLAlchemy```
    - Importa SQLAlchemy para la gestión de la base de datos.
- ```from flask_migrate import Migrate```
    - Importa Migrate para las migraciones de la base de datos.
- ```app = Flask(__name__)```
    - Crea una instancia de la aplicación Flask.
- ```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/repaso'```
    - Configura la URI de la base de datos MySQL.
- ```app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False```  
    - Desactiva el seguimiento de modificaciones.
- ```db = SQLAlchemy(app)```
    - Crea una instancia de SQLAlchemy.
- ```migrate = Migrate(app, db)```
    - Configura Flask-Migrate.
- ```import models```
    - Importa los modelos después de la inicialización de db y migrate.