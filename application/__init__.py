from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return '<h2>Hello World</h2>'
