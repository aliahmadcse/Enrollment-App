from application import app
from flask import render_template


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html")
