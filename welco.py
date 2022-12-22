from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "indeksas"
@app.route("/welcome")
def welcome():
    return "<p>welcome</p>"
@app.route('/welcome/home')
def home():
    return "<p>welcome home</p>"
@app.route('/welcome/back')
def back():
    return "<p>welcome back</p>"    