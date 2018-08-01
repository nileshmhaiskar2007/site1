from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
	lon =  []
	for i in range(21):
		lon.append(str(i))
	return render_template("index.html",lon = lon)


@app.route("/members")
def member():
	return render_template("members.html")


@app.route("/signup",methods = ["GET","POST"])
def signup():
	return render_template("signup.html")
	

@app.route("/contactus")
def contactus():
	return render_template("contactus.html")


@app.route("/result",methods = ["GET","POST"])
def result():
	if request.method == "POST":
		result = request.form
		return render_template("result.html", result = result)
	else:
		return "Please signin"


