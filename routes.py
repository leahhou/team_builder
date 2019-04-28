from flask import request, render_template, redirect, url_for, abort, send_from_directory
from server import app, system

from team_building_system import TeamBuildingSystem
from profile import Login
from algorithm import Person, basicSort
from event import Event
from forms import ProfileForm

class PersonData:
  def __init__(self):
    self.position = None
    self.languages = None
    self.experience = None
    self.objective = None

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
    # print(form.ideas.data)
    if request.method == 'POST':
        print("in this statement")
        fields = PersonData()
        form.populate_obj(fields)
        print(fields.languages)
        print(fields.position)
        print(fields.experience)

        # new = Person(id, languages, position, experience, objective, ideas)
        # system.add_profile(new)
        return redirect(url_for("profile", id=id))

    return render_template("preference_form.html", form=form, id=id)

@app.route("/profile/<id>")
def profile(id):
    profile = None
    username = None
    for i in system.profiles:
        if i.id == id:
            profile = i
            break
    for j in system.logins:
        if j.id == id:
            username = j.username
            print(username)
            break
    return render_template("profile.html", username=username, profile=profile)

@app.route("/all_members/id")
def all_members(id):
    for i in system.events:
        if i.id == id:
            event = i
            break
    return render_template("all_members.html", event=event)

@app.route("/all_teams/")
def all_teams():
    for i in system.events[0].teams:
        print(i)
    return render_template("all_teams.html", event=system.events[0], users=system.logins)

@app.route("/member_team/<event_id>/<id>")
def member_team(event_id, id):
    for i in system.events:
        if i.id == id:
            event = i
            break
    
    for j in event.teams:
        if j.id == id:
            team = j
            break
    return render_template("member_team.html", team=team, logins=system.logins)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/sort')
def sort():
    system.events[0].teams = basicSort(system.profiles, 4)
    return render_template("all_teams.html", event=system.events[0], users=system.logins)