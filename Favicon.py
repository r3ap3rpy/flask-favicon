import os
from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsof.icon')

@app.route("/")
def index():
	return render_template("index.html")
	