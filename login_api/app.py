import flask
from flask import redirect, render_template, request, session, url_for

app = flask.Flask(__name__)
app.secret_key = 'b1R0sC4'

#GET,POST - INDEX LOG IN
@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('user.html', username=username)

#GET,POST - LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST' and request.form['username'] != '':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

#GET,POST - LOGOFF
@app.route('/logoff')
def logoff():
    session.pop('username', '')
    return redirect(url_for('index'))

#GET,POST - CREATE
@app.route('/signup')
def signup():
    return render_template('signup.html')

#GET - USERS HOME
@app.route('/user/<username>')
def home(username):
    return render_template('user.html', user_name=username)

#GET,PUT - UPDATE SETTINGS
@app.route('/settings')
def update():
    return render_template('settings.html')

#GET,DELETE - DELETE CREDENCIALS
@app.route('/delete')
def delete():
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)