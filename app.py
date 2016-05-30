from flask import Flask, render_template, request, abort, redirect, Response
import json
import netease
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
