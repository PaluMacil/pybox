"""blog\__init__.py: This file initializes the auth Blueprint."""

__author__ = 'dan'

from flask import Blueprint

# Provide a blueprint object for dynamic import
blueprint = Blueprint('blog', __name__, template_folder='templates')
# Provide an alias for the blueprint for readable views
blog = blueprint

from . import views

# Access to main view
main = views.index
