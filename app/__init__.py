#dependecia de flask
from flask import Flask
#Dependecia de configuracion
from .config import Config

#dependecia de los modelos
from flask_sqlalchemy import SQLAlchemy
#dependecia para las migraciones
from flask_migrate import Migrate
from .mi_blueprint import mi_blueprint
from app.products import products


#crear el objeto flask
app = Flask(__name__)
#Configuracion del obgeto Flask
app.config.from_object(Config)

#vincular blueprints del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)


#crear el objeto de modelos
db = SQLAlchemy(app)
#crear el objeto de la migracion
migrate = Migrate(app, db)


#importar modelos de .models

from .models import Cliente, Producto, Detalle, Venta