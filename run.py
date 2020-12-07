from flask import Flask, render_template, request
from counts import charcount, specialcount, wordcount, linecount
from sorts import commonsort, alphasort
import datetime
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		text = request.form["text"]
		data = {
			"charcount": charcount(text),
			"charcount_nospace": charcount(text, spaces=False),
			"specialcount": specialcount(text),
			"wordcount": wordcount(text),
			"commonsort": commonsort(text),
			"alphasort": alphasort(text),
		}
		return render_template("index.html", data=data)
	if request.method == "GET":
		return render_template("index.html",)

if __name__ == "__main__":
	app.run()