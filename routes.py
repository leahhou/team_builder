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
          return redirect(url_for("preference.html"))
      return render_template("login.html")

@app.route("/preference/", method=["POST"])
  def preference(): 
      #database to store all options to display in form
      languages=["python","ruby"]
      return render_template("preference_form.html", languages=languages)

@app.route("/profile/<name>")
  def profile(name): 
      return render_template("profile.html")
