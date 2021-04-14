from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required     #If we are not logged in and try to visit the welcome page then the page redirects to login probing the user to login first
def welcome_user():
    return render_template('welcome.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()       #called that function from flask_login. So automatically done for us
    flash("You logged out!")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)    #imported the function
            flash("Logged in successfully!")
            #next holds the actual requested page of the user without logging in
            next = request.args.get('next')     #if a user tries to access the welcome page without logging in then first flask asks the user to login and then saves the welcome bage in next so that after login the user is immediately directed to that page

            if next == None or not next[0]=='/':
                next = url_for('welcome')
            
            return redirect(next)

    return render_template('login.html', form=form)


@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password =  form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for Registration!")

        return redirect(url_for(login))

    return render_template('register.html', form = form)


if __name__=="__main__":
    app.run(debug=True)

