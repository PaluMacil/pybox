"""app\__init__.py: This file initializes the Flask app."""

__author__ = 'dan'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import config
from os import path, listdir
from importlib import import_module

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .core import core as core_blueprint
    app.register_blueprint(core_blueprint)

    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/account')

    for blueprint in get_blueprint_tuples():
        print(blueprint)
        app.register_blueprint(blueprint[0], url_prefix=blueprint[1])

    return app


def get_blueprint_tuples():

    plugin_dir = path.join(path.dirname(__file__), 'pycans')

    import_string_list = [''.join(['.pycans.', d]) for d
                          in listdir(plugin_dir)
                          if path.isdir(path.join(plugin_dir, d))
                          and not d.startswith('__')]

    # The 'blueprints' list is composed of tuples with a blueprint object and url_prefix (string)
    blueprints = []
    for import_string in import_string_list:
        module = import_module(import_string, __package__)
        blueprints.append((module.blueprint, ''.join(['/', module.__name__.split('.')[2]])))
    return blueprints
