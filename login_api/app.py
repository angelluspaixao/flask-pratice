import flask
from flask import abort, redirect, render_template, request, url_for
#TO-DO: usar redirect e url_for pra HTTP CATS
#TO-DO: usar redirect de /login para /user/<user_name> se tiver sessão

app = flask.Flask(__name__)

#GET,POST - LOG IN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] == 'admin@admin.com' and request.form['pass'] == 'admin':
            return redirect(url_for('home'), code=302)
        else:
            abort(401) and redirect(url_for('https://http.cat/401'), code=401)
            #return render_template('login.html')
    else:
        abort(403, ) and redirect(url_for('https://http.cat/403'), code=403)
        #return render_template('login.html')

#GET,POST - CREATE
@app.route('/signup')
def signup():
    return render_template('signup.html')

#GET - USERS HOME
@app.route('/user/<user_name>')
def home(user_name):
    return render_template('user.html', user_name=user_name)

#GET,PUT - UPDATE SETTINGS
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