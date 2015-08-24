import os
from setuptools import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='pyboxio',
    version='0.0.1',
    packages=['app', 'app.blog', 'app.core', 'app.account'],
    url='https://github.com/PaluMacil/pybox',
    license='GPLv2',
    keywords="blog, cms, document management, content management",
    platforms="OS Independent",
    author='Dan Wolf',
    author_email='dcwolf@gmail.com',
    description='Pybox is a modular CMS with easy click-plugin support.',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ]
)
