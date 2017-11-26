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
    return [{"name": "Paris", "tagline": "Experience the world of Walt Disney", "image": "http://run.disneylandparis.com/sites/default/files/styles/news/public/event/n025044_2023sep21_hmdlp-disneyland-paris-10k_ok_1440x843_0.jpg?itok=W4OBi2De", "price": "300e", "flight-time": "2h 40 min", "description": "Paris has a timeless familiarity for first-time and frequent visitors, with instantly recognisable architectural icons, along with exquisite cuisine, chic boutiques and priceless artistic treasures."},{"name": "Shanghai", "tagline": "Discover the largest commercial center in China", "image": "https://lonelyplanetwp.imgix.net/2017/03/Shanghai_for_free-abe6e2eb510b.jpg?crop=entropy&fit=crop&h=421&sharp=10&vib=20&w=748", "price": "450e", "flight-time": "5h 40 min", "description": "Shanghai, on China’s central coast, is the country's biggest city and a global financial hub. Its heart is the Bund, a famed waterfront promenade lined with colonial-era buildings. Across the Huangpu River rises the Pudong district’s futuristic skyline, including 632m Shanghai Tower and the Oriental Pearl TV Tower, with distinctive pink spheres. Sprawling Yu Garden has traditional pavilions, towers and ponds."},{"name": "New York", "tagline": "Spend a weekend in the Big Apple", "image": "https://media-cdn.tripadvisor.com/media/photo-s/0e/9a/e3/1d/freedom-tower.jpg", "price": "550e", "flight-time": "6h 40 min", "description": "New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean. At its core is Manhattan, a densely populated borough that’s among the world’s major commercial, financial and cultural centers. Its iconic sites include skyscrapers such as the Empire State Building and sprawling Central Park. Broadway theater is staged in neon-lit Times Square."}, {"name": "Tokyo", "tagline": "Tokyo mixes the ultramodern and the traditiona", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS42P2nCkk6-wnrKB8gMcGSHG1J9eGKD4Jae7lH2if8k5gtphw_", "price": "500e", "flight-time": "7h 40 min", "description": "Tokyo, Japan’s busy capital, mixes the ultramodern and the traditional, from neon-lit skyscrapers to historic temples. The opulent Meiji Shinto Shrine is known for its towering gate and surrounding woods. The Imperial Palace sits amid large public gardens. The city's many museums offer exhibits ranging from classical art (in the Tokyo National Museum) to a reconstructed kabuki theater (in the Edo-Tokyo Museum)."},{"name": "Gran Canaria", "tagline": "Get some sun at Gran Canaria", "image": "https://www.riu.com/en/binaris/Gran-canaria2_tcm55-27954.jpg", "price": "700e", "flight-time": "5h 00 min", "description": "Gran Canaria is the third largest island in the Canary Islands and has the largest population. It's often described as a "continent in miniature" because it has so much variety to offer."},{"name": "Sydney", "tagline": "Sydney is the largest and oldest city in Australia.", "image": "https://int.sydney.com/sites/international/files/styles/header_slider/public/2016-12/Sydney-Harbour.jpg?itok=QmFhEdGP", "price": "800e", "flight-time": "11h 10 min", "description": "Brimming with history, nature, culture, art, fashion, cuisine, design, Sydney's set next to miles of ocean coastline and sandy surf beaches. Longterm immigration has led to the cities reputation as one of the most culturally and ethnically diverse cities in Australia and the world. The city is also home to the Sydney Opera House and the Sydney Harbour Bridge, two of the most iconic structures on this planet."}]

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