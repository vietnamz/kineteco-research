import os

from flask import Flask
from flask_restplus import Api, Namespace
from flask_sqlalchemy import SQLAlchemy

from service.config import app_config

db = SQLAlchemy()
config_name = os.getenv('APP_SETTINGS')

app = Flask(__name__)

monitoring_namespace = Namespace(
    "monitoring",
    description="Monitoring and health check data"
)
api = Api(app, doc='/docs', title='Research API')
api.add_namespace(monitoring_namespace)
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from service.views import health

db.init_app(app)
