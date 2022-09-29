import flask
from flask import render_template

app = flask.Flask(__name__)

#GET,POST - LOG IN
@app.route('/')
def login():
    return render_template('login.html')

#GET,POST - CREATE
@app.route('/signup')
def signup():
    return render_template('signup.html')

#GET - USERS HOME
@app.route('/user/<user_name>')
def home(user_name):
    return render_template('user.html', user_name=user_name)

#GET,POST - UPDATE SETTINGS
@app.route('/settings')
def update():
    return render_template('settings.html')

#GET,POST - LOG OFF
@app.route('/logoff')
def logoff():
    return render_template('logoff.html')

#GET,DELETE - DELETE CREDENCIALS
@app.route('/delete')
def delete():
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)