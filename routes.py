from flask import flask, request, render_template, url_for, abort
from server import app, system

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login", method=["POST"])
  def login: 
      if request.method == "POST":
          # retrieve login details
          username = request.form["username"]
          password = request.form["password"]
          print(username,password)

          return redirect(url_for("preference.html"))
      return render_template("login.html")

@app.route("/preference/<name>", method=["POST"])
  def preference(name): 
      return render_template("preference_form.html")

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
