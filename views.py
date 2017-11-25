#encoding: utf-8
from flask import Flask
from flask import render_template
import sqlite3
import os
import json
from flask import g, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
DATABASE = os.path.join(BASE_DIR, 'finnair.db')


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_trips():
    #Todo: get proper recommendations
    return [{"name": "Paris", "tagline": "Experience the world of Walt Disney", "image": "http://run.disneylandparis.com/sites/default/files/styles/news/public/event/n025044_2023sep21_hmdlp-disneyland-paris-10k_ok_1440x843_0.jpg?itok=W4OBi2De", "price": "300e", "flight-time": "2h 40 min", "description": "Paris has a timeless familiarity for first-time and frequent visitors, with instantly recognisable architectural icons, along with exquisite cuisine, chic boutiques and priceless artistic treasures."}]

def get_destination_info(destination):
    pass

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    query = request.args.get('query')
    if query == "trips":
        trips = get_trips()
        return jsonify(trips)
    elif query == "info":
        destination_info = get_destination_info(request.args.get('destination'))
        return jsonify(destination_info)

    return "", 501


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)