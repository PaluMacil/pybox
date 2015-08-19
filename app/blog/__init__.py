"""blog\__init__.py: This file initializes the auth Blueprint."""

__author__ = 'dan'

from flask import Blueprint

blog = Blueprint('blog', __name__)

from . import views
