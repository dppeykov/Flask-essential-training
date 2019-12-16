from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  # the template html needs to be in the /templates folder in the project - not included in this repo - e.g. /templates/home.html
  return render_template("template-home.html") # by adding , name="X-men" in the () we can pass the value to the html template 


@app.route('/your-url', methods=["GET", "POST"])
def your_url():
  if request.method == "POST":
    return render_template("template-your_url.html", code=request.form["code"]) 
# a get request in the template-home.html will call the your-url function and pass the code variable to the template-your_url.html
  else:
    # return redirect("/") # redirecting the user to the homepage
    return redirect(url_for("home")) # a different way to redirect - allows the / to be changed and the code to still work - 
    # home is the name of the function in the home route

