"""account\views.py: This file contains the auth views."""

__author__ = 'dan'

from . import account


@account.route('/login')
def login():
    return "login page!"
