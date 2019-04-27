from flask import render_template, request, redirect, url_for, abort
from server import app, system

@app.route('/')
def homepage():
    return render_template('index.html')