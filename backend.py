import os
import requests
import json
import string
from flask import Flask, redirect, url_for, flash, render_template, request 
from dotenv import load_dotenv, find_dotenv
from google.cloud import vision

load_dotenv(find_dotenv())

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fake-article-detect-15937-caffac9b5baf.json'
API_KEY = os.getenv('NYT_API_KEY')

app = Flask(__name__)
app.secret_key = 'potato_jackson_lemon_stevey'
links = ['init']

'''Google Cloud Vision API used to extract text from article image'''
def detect_text(file_name): 
    
    client = vision.ImageAnnotatorClient()
    content = file_name.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    text_data = texts[0].description
    print(text_data)
    return text_data

'''Search for NYT article by body text.'''
def nyt_api(text):
    NYT_REQUEST = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(
        NYT_REQUEST,
        headers=headers,
        params={
            'q': text,
            'api-key': API_KEY
        }
    )
    json_data = response.json()
    nyt_article_link = ''
    if (json_data['response']['docs'] == []):
        nyt_article_link = 'fake'
    else:
        nyt_article_link = str(json_data['response']['docs'][0]['web_url'])

    return nyt_article_link

'''Routing for home page'''
@app.route('/')
def main():
    return render_template('index.html', results = links)

@app.route('/upload', methods = ["GET", "POST"])
def handle_file():
    img = request.files['input-image']
    if img.filename == '':
        flash('Please upload an image before submitting')
        return redirect(url_for('main'))
    
    global nyt_detect
    global links
    links.clear()
    img_text = detect_text(img)
    img_text = img_text.replace('\n', ' ')
    x = -50
    for i in range(3):
        temp = nyt_api(img_text[x:])
        if temp != 'fake' and temp not in links:
            links.append(temp)
        x = x - 19
    if len(links) == 0:
        links.append('FAKE NEWS!')
    return redirect(url_for('main'))

'''Profile Pages for Group Members'''
@app.route('/gabe')
def gabe():
    return render_template('gabe.html')

@app.route('/dullah')
def dullah():
    return render_template('dullah.html')

@app.route('/brian')
def brian():
    return render_template('brian.html')

@app.route('/zaid')
def zaid():
    return render_template('zaid.html')

@app.route('/zach')
def zach():
    return render_template('zach.html')

app.run()