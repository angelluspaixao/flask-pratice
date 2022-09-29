import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def login():
    return '<h1>Login</h1>'

app.run()