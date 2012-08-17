from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from os import environ

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hotspots')
def get_hotspots():
    networks = [
        ['abc', 32.0833, 34.8000],
        ['def', 32.0800, 34.7960],
        ['ghi', 32.0840, 34.7930],
    ]
    return jsonify(networks=networks)


@app.route('/hotspots/add', methods=['POST'])
def add_network():
    fields = ['lat', 'lng', 'ssid', 'password']
    vals = [request.form[k] for k in fields]
    try:
        print vals
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
