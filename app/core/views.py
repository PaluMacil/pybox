"""core\views.py: This file contains the main views."""

__author__ = 'dan'

from flask import send_from_directory, render_template, g, request
from . import core
from .models import Pycan, Setting
from os import path


@core.route('/')
def index():
    post = render_template('widgets/post.html')
    return render_template('index.html', author='Dan Wolf', post=post)


@core.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(core.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@core.before_app_request
def load_globals():
    # Don't load globals when handling static requests
    if '/static/' not in request.path:
        g.settings = Setting.as_list()
        g.pycans = Pycan.as_dict()
        print(g.pycans)


@core.before_request
def print_endpoint():
    print(request.endpoint)
