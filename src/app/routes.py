from app.database.models import Example
from app import app
from flask import json, render_template, request, url_for, jsonify

@app.route("/", methods=["GET"])
@app.route('/home', methods=['GET'])
def render_home():
    return render_template("index.html")
