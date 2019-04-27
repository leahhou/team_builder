from flask import render_template, request, redirect, url_for
from server import app, system

@app.route('/')
def homepage():
    return render_template('index.html')