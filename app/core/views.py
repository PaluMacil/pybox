"""core\views.py: This file contains the main views."""

__author__ = 'dan'

from flask import send_from_directory, render_template, g
from os.path import join
from . import core
from .models import Pycan, Setting


@core.route('/')
def index():
    post = render_template('widgets/post.html')
    return render_template('index.html', author='Dan Wolf', post=post)


@core.route('/favicon.ico')
def favicon():
    return send_from_directory(join(core.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@core.before_app_request
def load_globals():
    g.settings = Setting.as_list()
    g.pycans = Pycan.as_list()
    var = g.__dict__
    print(var)
    var2 = var