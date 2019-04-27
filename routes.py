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
    print(form.validate())
    print(form.ideas.data)
    if request.method == 'POST':
        print("in this statement")
        position = form.position.data
        languages = form.languages.data
        experience = form.experience.data
        objective = form.objective.data
        ideas = 1

        new = Person(id, languages, position, experience, objective, ideas)
        system.add_profile(new)
        return redirect(url_for("profile", id=id))

    return render_template("preference_form.html", form=form, id=id)

@app.route("/profile/<id>")
def profile(id):
    for i in system.profiles:
        if i.id == id:
            profile = i
            break
    for j in system.logins:
        if j.id == id:
            username = j.username
            break
    return render_template("profile.html", username=username, profile=profile)

@app.route("/all_members/id")
def all_members(id):
    for i in system.events:
        if i.id == id:
            event = i
            break
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