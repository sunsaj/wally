from app import app
from flask import render_template
import requests

@app.route('/')
def index():
    API_KEY = '563492ad6f91700001000001ff99f2e572fd45b88df7fc8bd682006e'
    url = 'https://api.pexels.com/v1/search'            
    params = dict(query='sunset')
    headers = dict(Authorization=API_KEY)
    data = requests.get(url, headers=headers, params=params).json()
    
    return render_template("index.html", title='Me', data=data)

def wall(id):
    return render_template("wall.html")
