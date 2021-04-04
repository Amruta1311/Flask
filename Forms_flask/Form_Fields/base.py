from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                     RadioField, SelectField, TextField, 
                     TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField("what breed are you?", validators=[DataRequired()]) #Ensures that the form has a value entered by the user
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mood:", choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u"Pick your favourite food:", choices = [('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')]) #U is written right before the string to ensure we dont get any errors
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data      
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))        # redirects to the thankyou only after the valid submission

    return render_template('index.html', form = form)

@app.route('/thankyou')

def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
