from application import app

@app.route('/')
@app.route('/index')
def hello_world():
    return '<h2>Hello World</h2>'
