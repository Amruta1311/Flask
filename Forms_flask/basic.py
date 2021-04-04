from flask import Flask, render_template
from flask_wtf import FlaskForm                 #FlaskForm is the class that we are going to inherit from to create our own forms
from wtforms import StringField, SubmitField    #For submitting the form 

app = Flask(__name__)

# We need to configure a secret key in order to CSRF security work

app.config['SECRET_KEY'] = 'mysecretkey' # This is a key that is built into the flask application configuration and we can set this to any string that we want

# We create an instance of the wtform class and later set a view function that creates the instance of that form class and then checks if it is a valid submission

class InfoForm(FlaskForm):                           # InfoForm inherits from the FlaskForm
    breed = StringField("What breed are you?")       # We basically inport certain fields from the wtforms and later provide the parameters related to that field
    submit = SubmitField("Submit")                   # In this case. the breed is the attribute to the InfoForm

@app.route('/', methods=['GET','POST']) # This is going to allow to pass in this form to the template

def index():
    breed = False       # Here breed is a simple variable and different from the breed used in the InfoForm

    form = InfoForm()   # Here we create the instance of the form

    if form.validate_on_submit():
        breed = form.breed.data     # Returns the data submitted for the breed field of InfoForm
        form.breed.data = ''

    return render_template('index.html', form = form, breed = breed)

if __name__ == '__main__':
    app.run(debug=True)