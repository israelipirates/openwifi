from flask import Flask, render_template, request, jsonify
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
    return jsonify(hotspots=hotspots)


@app.route('/hotspots/add', methods=['POST'])
def add_hotspot():
    fields = ['ssid', 'password', 'lat', 'lng']
    vals = [request.form.get(k) for k in fields]
    try:
        return jsonify(vals=vals)
        #hotspot.create(*vals)
    except:
        return jsonify(res='err')
    return jsonify(res='ok')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
