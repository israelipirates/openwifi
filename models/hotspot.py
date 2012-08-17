from app import db


class Hotspot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssid = db.Column(db.String(80))
    password = db.Column(db.String(120))
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())

    def __init__(self, ssid, password, lat, lng):
        self.ssid = ssid
        self.password = password
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<Hotspot %r>' % self.ssid
