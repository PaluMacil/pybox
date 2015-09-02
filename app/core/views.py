"""core\views.py: This file contains the main views."""

__author__ = 'dan'

from flask import send_from_directory, render_template, g, request
from . import core
from .models import Pycan, Setting
from os import path


@core.route('/')
def index():
    main_page_pycan = g.settings.get('CORE.MAIN.FRONTPAGE')
    if main_page_pycan:
        return g.pycans[main_page_pycan].package.main()
    else:
        return 'This page does not exist', 404


@core.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(core.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@core.before_app_request
def load_globals():
    # Don't load globals when handling static requests
    if '/static/' not in request.path:
        g.settings = Setting.as_dict()

        g.pycans = Pycan.as_dict()
        print(g.pycans)


@core.before_request
def print_endpoint():
    print(request.endpoint)
