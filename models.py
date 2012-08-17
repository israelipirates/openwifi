from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hotspot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssid = db.Column(db.String(80))
    password = db.Column(db.String(120))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    created = db.Column(db.Date, default=datetime.now)
    updated = db.Column(db.Date, onupdate=datetime.now)

    def __init__(self, ssid, password, lat, lng):
        self.ssid = ssid
        self.password = password
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<Hotspot %r>' % self.ssid
