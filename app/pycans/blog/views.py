"""blog\views.py: This file contains the views related to the blog module."""

__author__ = 'dan'

from flask import render_template
from . import blog


@blog.route('/')
def index():
    post = render_template('widgets/post.html')
    return render_template('index.html', author='Dan Wolf', post=post)


@blog.route('/test')
def test():
    return render_template('blog/user.html')
