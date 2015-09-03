"""page\views.py: This file contains the pages related to the page module."""

__author__ = 'dan'

from flask import render_template
from . import page


@page.route('/')
def index():
    return render_template('page/user.html')


