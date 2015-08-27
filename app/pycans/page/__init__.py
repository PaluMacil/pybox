"""page\__init__.py: This file initializes the page Blueprint."""

__author__ = 'dan'

from flask import Blueprint

blueprint = Blueprint('page', __name__)

from . import views
