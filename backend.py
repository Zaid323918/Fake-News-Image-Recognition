import os
import requests
import json
import string
from flask import Flask, redirect, url_for, flash, render_template, request 
from dotenv import load_dotenv, find_dotenv
from google.cloud import vision

load_dotenv(find_dotenv()) #Finds .env file 

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fake-article-detect-15937-caffac9b5baf.json' #Replace with the name of your json file
API_KEY = os.getenv('NYT_API_KEY')

app = Flask(__name__)
app.secret_key = 'potato_jackson_lemon_stevey' #Required for Flask to keep sessions
links = ['init']

'''Google Cloud Vision API used to extract text from article image.'''
def detect_text(file_name): 
    
    client = vision.ImageAnnotatorClient()
    content = file_name.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    text_data = texts[0].description
    return text_data

'''Searches for NYT article by body text.'''
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
            'begin_date': '19500101', 
            'api-key': API_KEY
        }
    )
    json_data = response.json()
    nyt_article_link = ''
    if (json_data['response']['docs'] == []): #No article found
        nyt_article_link = 'fake'
    else:
        nyt_article_link = str(json_data['response']['docs'][0]['web_url']) #The URL of the article found

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
    
    global links
    links.clear()
    img_text = detect_text(img)
    img_text = img_text.replace('\n', ' ')
    x = -37
    for i in range(3):
        while img_text[x] != ' ': #Ensuring query string is complete words
            x = x - 1
        query_text = '"' + img_text[x:] + '"' #Adding quotation marks to query string 
        temp = nyt_api(query_text) #Searches for potential matches using different amounts of text to increase chances of success
        if temp != 'fake' and temp not in links:
            links.append(temp)
        x = x - 19
    if len(links) == 0: #No articles found by the NYT API
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