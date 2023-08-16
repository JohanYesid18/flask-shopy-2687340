#dependecia de flask
from flask import Flask
#Dependecia de configuracion
from .config import Config

#dependecia de los modelos
from flask_sqlalchemy import SQLAlchemy
#dependecia para las migraciones
from flask_migrate import Migrate

#crear el objeto flask
app = Flask(__name__)
#Configuracion del obgeto Flask
app.config.from_object(Config)


#crear el objeto de modelos
db = SQLAlchemy(app)
#crear el objeto de la migracion
migrate = Migrate(app, db)

#importar modelos de .models

from .models import Cliente, Producto, Detalle, Venta