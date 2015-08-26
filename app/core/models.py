"""core\models.py: This file contains models relating to site settings and the main landing page"""

__author__ = 'dan'

from .. import db


class Setting(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    blueprint = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)
    value = db.Column(db.String(64))

    @classmethod
    def as_list(cls):

        settings_list = cls.query.all()

        return settings_list


class Pycan(db.Model):
    __tablename__ = 'pycans'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    packagename = db.Column(db.String(64), unique=True, index=True)
    status = db.Column(db.String(64), default='INACTIVE')
    description = db.Column(db.Text)

    @classmethod
    def as_list(cls, only_active=True):
        if only_active:
            pycan_list = cls.query.filter_by(status='ACTIVE').all()
        else:
            pycan_list = cls.query.all()

        return pycan_list
