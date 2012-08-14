import os

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from models import hotspot

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/networks')
def get_networks():
    networks = [
        ['abc', 32.0833, 34.8000],
        ['def', 32.0800, 34.7960],
        ['ghi', 32.0840, 34.7930],
    ]
    return jsonify(networks=networks)


@app.route('/networks/add', methods=['POST'])
def add_network():
    fields = ['lat', 'lng', 'name', 'password']
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
