import os
import io
import requests
import json
import flask
from dotenv import load_dotenv, find_dotenv

from google.cloud import vision_v1
from google.cloud.vision_v1 import enums
from google.oauth2 import service_account

app = flask.Flask(__name__)

#Dullah
def detect_text(file_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/api_key.json'

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

@app.route('/')
def main():
    detect_text('/path/to/image.jpg')
    return flask.render_template('index.html')

app.run()