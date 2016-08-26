from gevent import monkey

async_mode = 'gevent'
monkey.patch_all()

from flask_restful import Api
from config.parser import Properties

from flask import Flask

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('application.cfg', silent=False)
properties = Properties()

api = Api(app)

from api.help import HelpApi

api.add_resource(HelpApi, '/api/help')
