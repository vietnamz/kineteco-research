import os

from flask import Flask
from flask_restplus import Api, Namespace
from flask_sqlalchemy import SQLAlchemy

from research.config import app_config

db = SQLAlchemy()
config_name = os.getenv('APP_SETTINGS')

app = Flask(__name__)

solar_namespace = Namespace(
    "solar",
    description="Endpoints for solar panel data"
)
monitoring_namespace = Namespace(
    "monitoring",
    description="Monitoring and health check data"
)
api = Api(app, doc='/docs', title='KinetEco Research API')
api.add_namespace(monitoring_namespace)
api.add_namespace(solar_namespace)
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from research.views import health, solar

db.init_app(app)
