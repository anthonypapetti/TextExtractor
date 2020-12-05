from flask import Flask, render_template, request
from counts import charcount, specialcount, wordcount
import datetime
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		text = request.form["text"]
		return render_template("index.html")
	if request.method == "GET":
		data = 1
		return render_template("index.html", data=data)

if __name__ == "__main__":
	app.run()