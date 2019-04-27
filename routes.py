from flask import request, render_template, redirect, url_for, abort, send_from_directory
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
                    return redirect(url_for("preference", id=i.id))
                else:
                    errors = {}
                    errors["login"] = "Login failed"
                return render_template("login.html", errors=errors)
    return render_template("login.html")

@app.route("/preference/<id>", methods=["POST","GET"])
def preference(id): 
    form = ProfileForm()
    if request.method == 'POST' and form.validate() and form.submit.data:
        position = form.position.data
        languages = form.languages.data
        experience = form.experience.data
        objective = form.objective.data
        ideas = form.ideas.data

        new = Person(id, languages, position, experience, objective, ideas)
        system.add_profile(new)
        return redirect(url_for("profile"), id)


    return render_template("preference_form.html", form=form)

@app.route("/profile/<id>")
def profile(id):
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

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)