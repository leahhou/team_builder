from flask import request, render_template, redirect, url_for, abort
from server import app, system

from team_building_system import TeamBuildingSystem
from profile import Login
from algorithm import Person
from event import Event
from forms import ProfileForm

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # retrieve login details
        username = request.form["username"]
        password = request.form["password"]
        
        for i in system.logins:
            if i.username == username:
                if i.verify(username, password):
                    return redirect(url_for("preference"))
                else:
                    errors = {}
                    errors["login"] = "Login failed"
                return render_template("login.html", errors=errors)
    return render_template("login.html")

@app.route("/preference", methods=["POST","GET"])
def preference(): 
    form = ProfileForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template("preference_form.html", form=form)

@app.route("/profile/<name>")
def profile(name): 
      return render_template("profile.html")

@app.route("/all_members/<name>")
def all_members(name): 
      return render_template("all_members.html")

@app.route("/all_teams/<name>")
def all_teams(name): 
      return render_template("all_teams.html")

@app.route("/member_team/<name>")
def member_team(name): 
      return render_template("member_team.html")