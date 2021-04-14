#Since we are dealing with open authorization locally, we need to set up some environmetn variables
# This won't be the case if we are going to deploy the app
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

###############################################################################

from flask import Flask, redirect, render_template, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='363933465849-kv2jm4slivt9l6bju2vb6j64q09evihk.apps.googleusercontent.com', client_secret='k3xmhxIOlF-U6yh5VbCYiDjK', offline=True, scope=['profile','email'])

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')

def index():
    render_template('home.html')


@app.route('/welcome')
def welcome():
    #RETURN ERROR INTERNAL SERVER ERROR IF NOT LOGGED IN
    resp = google.get('/oauth/v2/userinfo')
    assert resp.ok, resp.text   #will return an error if someone is not logged 
    email = resp.json()["email"]    #grabs the email of whoever logged in
    return render_template('welcome.html', email = email)


@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))  # Flask takes you to the screen to ask you about your google credentials
    resp = google.get('/oauth/v2/userinfo')
    assert resp.ok, resp.text   #records the response which is essentially a json file
    email = resp.json()["email"]    #grabs the email of whoever logged in

    return render_template('welcome.html', email = email)

if __name__=="__main__":
    app.run()