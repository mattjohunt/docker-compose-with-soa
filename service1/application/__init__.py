from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/request')
def route():

    r = requests.get("http://service2:5000")

    return r.text