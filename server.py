from flask import Flask
from init import bootstrap_system

app = Flask(__name__)
app.secret_key = 'very-secret-123'

system = bootstrap_system()