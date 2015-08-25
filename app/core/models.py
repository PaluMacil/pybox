"""core\models.py: This file contains models relating to site settings and the main landing page"""

__author__ = 'dan'

from .. import db


class Setting(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    blueprint = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)


class Pycan(db.Model):
    __tablename__ = 'pycans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    packagename = db.Column(db.String(64), unique=True, index=True)
    blueprint = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)

    @property
    def pycan_list(self):
        raise NotImplementedError('pycan_list is not yet implemented')

    @pycan_list.setter
    def pycan_list(self, password):
        raise AttributeError('pycan_list is not a settable attribute')
