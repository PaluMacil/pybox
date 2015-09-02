"""blog\__init__.py: This file initializes the auth Blueprint."""

__author__ = 'dan'

from flask import Blueprint
from importlib import import_module

# Provide a blueprint object for dynamic import
blueprint = Blueprint('blog', __name__)
# Provide an alias for the blueprint for readable views
blog = blueprint

from . import views

main = views.index
