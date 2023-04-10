import os
import io
import requests
import json
from flask import Flask, redirect, url_for, flash, render_template, request 
from dotenv import load_dotenv, find_dotenv

from google.cloud import vision_v1
#from google.cloud.vision_v1 import enums #THIS IS CAUSING ISSUE SO I COMMENTED OUT
from google.oauth2 import service_account

app = Flask(__name__)

#Dullah's code stuff
def detect_text(file_path): 
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/api_key.json' #path needs fixing and api key needs to be hidden. 

    credentials = service_account.Credentials.from_service_account_file('/path/to/api_key.json')

    client = vision_v1.ImageAnnotatorClient(credentials=credentials)

    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print('Texts:')
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
    return

#Zach
def nyt_api():
    return

#these render the profile pages for each of us!
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

@app.route('/')
def main():
    detect_text('/path/to/image.jpg')
    return render_template('index.html')

app.run()