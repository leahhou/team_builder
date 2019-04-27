from flask import request, render_template, redirect, url_for, abort
from server import app, system

from team_building_system import TeamBuildingSystem
from algorithm import Person
from event import Event

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login", method=["POST"])
def login():
    if request.method == "POST":
        # retrieve login details
        username = request.form["username"]
        password = request.form["password"]
        
        for i in 

        return redirect(url_for("preference"))
    return render_template("login.html")

@app.route("/preference/<name>", method=["POST"])
def preference(name): 
    return render_template("preference_form.html")

@app.route("/profile/<name>")
def profile(name): 
    return render_template("profile.html")
