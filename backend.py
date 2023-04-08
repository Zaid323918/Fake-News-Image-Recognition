import os
import requests
import json
import flask
from dotenv import load_dotenv, find_dotenv

app = flask.Flask(__name__)

#Dullah
def vision_api():
    return

#Zach
def nyt_api():
    return

@app.route('/')
def main():
    return flask.render_template('index.html')

app.run()