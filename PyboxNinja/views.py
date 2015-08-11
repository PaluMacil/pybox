__author__ = 'dan'

from PyboxNinja import app
from flask import send_from_directory
from os.path import join


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/css/<path:filename>')
def send_css(filename):
    path = join(app.static_folder, 'css')
    return send_from_directory(path, filename)


@app.route('/images/<path:filename>')
def send_image(filename):
    path = join(app.static_folder, 'images')
    print(path, end='\n')
    print(filename, end='\n')
    return send_from_directory(path, filename)


@app.route('/js/<path:filename>')
def send_js(filename):
    path = join(app.static_folder, 'js')
    return send_from_directory(path, filename)
