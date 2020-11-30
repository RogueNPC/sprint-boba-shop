from flask import Flask, request, render_template
from PIL import Image, ImageFilter
from pprint import PrettyPrinter
from dotenv import load_dotenv
import json
import os
import random
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    """The homepage"""
    return render_template('home.html')

@app.route('/about')
def aboutpage():
    """About us"""
    return render_template('about.html')

@app.route('/menu')
def menupage():
    """Our menu"""
    return render_template('menu.html')

@app.route('/contact')
def contactpage():
    """How to contact"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)