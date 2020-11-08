from app import app
from flask import render_template, request, redirect
import requests, json

@app.route('/')
def index():
    API_KEY = '563492ad6f91700001000001ff99f2e572fd45b88df7fc8bd682006e'
    url = 'https://api.pexels.com/v1/search'    
    query='nature'        
    params = dict(query=query, per_page=13)
    headers = dict(Authorization=API_KEY)
    data = requests.get(url, headers=headers, params=params).json()
    with open('json/data.json', 'w') as f:
        json.dump(data, f)
    
    return render_template("index.html", data=data, query=query)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    API_KEY = '563492ad6f91700001000001ff99f2e572fd45b88df7fc8bd682006e'
    url = 'https://api.pexels.com/v1/search'            
    params = dict(query=query,per_page=13)
    headers = dict(Authorization=API_KEY)
    data = requests.get(url, headers=headers, params=params).json()
    with open('json/data.json', 'w') as f:
        json.dump(data, f)
    
    return render_template("index.html", data=data, query=query)

@app.route('/view/<int:current_index>/<query>/<next>')
@app.route('/view/<int:id>/<query>')
def view(query, current_index=None, id=None, next=None):
    with open('json/data.json') as f:
        data = json.load(f)
    img =None
    if id:
        for i in range(len(data['photos'])):
            if id == data['photos'][i]['id']:
                id_index = i
    else:
        if next == 'forward' and current_index < 12:
            current_index += 1
        elif next=='backward' and current_index !=0:
            current_index -= 1
        
        id_index = current_index

    return render_template("index.html", data=data, id_index = id_index, query=query)


@app.route('/nav/<int:page>/<query>')
def nav(page,query):
    API_KEY = '563492ad6f91700001000001ff99f2e572fd45b88df7fc8bd682006e'
    url = 'https://api.pexels.com/v1/search'            
    params = dict(query=query, page=page, per_page=13)
    headers = dict(Authorization=API_KEY)
    data = requests.get(url, headers=headers, params=params).json()
    with open('json/data.json', 'w') as f:
        json.dump(data, f)
    
    return render_template("index.html", data=data, query=query)


@app.route('/download/<int:id_index>', methods=['POST'])
def download(id_index):
    size = request.form['size']
    with open('json/data.json') as f:
        data = json.load(f)

    url = data['photos'][id_index]['src'][size]
    return redirect(url)