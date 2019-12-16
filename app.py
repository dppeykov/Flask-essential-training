from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  # the template html needs to be in the /templates folder in the project - not included in this repo - e.g. /templates/home.html
  return render_template("template-home.html") # by adding , name="X-men" in the () we can pass the value to the html template 


@app.route('/your-url')
def your_url():
  return render_template("template-your_url.html", code=request.args["code"]) 
# a get request in the template-home.html will call the your-url function and pass the code variable to the template-your_url.html

