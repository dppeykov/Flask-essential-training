from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("template-home.html") # needs to be in the /templates folder in the project - not included in this repo - e.g. /templates/home.html

@app.route('/about')
def about():
  return "This is a URL shortener"
