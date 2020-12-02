from flask import Flask, render_template, request
from counts import charcount, specialcount, wordcount
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		text = request.form["text"]
		return render_template("index.html")
	if request.method == "GET":
		return render_template("index.html")

if __name__ == "__main__":
	app.run()