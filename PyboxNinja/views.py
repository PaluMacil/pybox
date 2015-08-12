__author__ = 'dan'

from PyboxNinja import app
from flask import send_from_directory, render_template
from os.path import join


@app.route('/')
def index():
    return render_template('index.html', author='Dan Wolf')


@app.route('/static/<folder>/<path:filename>')
def send_static(folder, filename):
    path = join(app.static_folder, folder)
    return send_from_directory(path, filename)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
