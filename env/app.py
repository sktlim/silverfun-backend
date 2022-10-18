import main
import flask

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def post_method():
    if request.method == 'POST':
        geojson = request.files['data']
        return main.find_nearest_points(geojson)

 
 