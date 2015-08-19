"""core\views.py: This file contains the main views."""

__author__ = 'dan'

from flask import send_from_directory, render_template
from os.path import join
from . import core


@core.route('/')
def index():
    post = render_template('post.html')
    return render_template('index.html', author='Dan Wolf', post=post)


@core.route('/favicon.ico')
def favicon():
    return send_from_directory(join(core.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
