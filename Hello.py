from flask import Flask     #From the flask package import the Flask class
app = Flask(__name__)       #Creates an 'app' object of instance class Flask imported from the flask package

@app.route('/')             #Decorator links the below page to whatever route on the web application. Here we have directed to homepage '/'   
                            #The string parameter passed into the decorator determines the url extension that will link to the function
def index():
    return '<h1>Hello Puppy!</h1>'      #Defines a page named index with the function returning a string

@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return '<h1>This is a page for {}</h1>'.format(name.upper())

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    pupname = ''
    if name[-1] == 'y':     #If last letter of name 
        pupname = name[:-1] + 'iful'    #All the way upto but not including the last letter
    else:
        pupname = name + 'y'
    return '<h1>This is a page for {}</h1>'.format(pupname.upper())

if __name__ == '__main__':  #If we are running the script then the aboe gets executed by app.run()
    app.run(debug=True)     #Helps us catch the errors if any on the webpage