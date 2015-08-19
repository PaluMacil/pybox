"""account\__init__.py: This file initializes the auth Blueprint."""

__author__ = 'dan'

from flask import Blueprint

account = Blueprint('account', __name__)

from . import views
