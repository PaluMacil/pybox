"""page\__init__.py: This file initializes the page Blueprint."""

__author__ = 'dan'

from flask import Blueprint

# Provide a blueprint object for dynamic import
blueprint = Blueprint('page', __name__)
# Provide an alias for the blueprint for readable views
page = blueprint

from . import views

main = views.index
