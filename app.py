from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  # the template html needs to be in the /templates folder in the project - not included in this repo - e.g. /templates/home.html
  return render_template("template-home.html") # by adding , name="X-men" in the () we can pass the value to the html template 



@app.route('/about')
def about():
  return "This is a URL shortener"
