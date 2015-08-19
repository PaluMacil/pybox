"""account\models.py: This file contains models relating to the account and authorization"""

__author__ = 'dan'

from flask.ext.login import UserMixin, AnonymousUserMixin
from .. import db, login_manager
