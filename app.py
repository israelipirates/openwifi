from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_heroku import Heroku
from os import environ

from models import db, Hotspot


app = Flask(__name__)
heroku = Heroku(app)

# hack for local dev
# see https://github.com/kennethreitz/flask-heroku/issues/8
if 'DATABASE_URL' not in environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hotspots')
def get_hotspots():
    hotspots = Hotspot.query.all()
    res = [hotspot.serialize() for hotspot in hotspots]
    return jsonify(hotspots=res)


@app.route('/hotspots/add', methods=['POST'])
def add_hotspot():
    fields = ['ssid', 'password', 'lat', 'lng']
    vals = dict([(k, request.form.get(k)) for k in fields])
    try:
        hotspot = Hotspot(**vals)
        db.session.add(hotspot)
        db.session.commit()
    except:
        pass
    return redirect(url_for('home'))


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
