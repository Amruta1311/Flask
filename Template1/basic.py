from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    constant = "Amruta Mulay"
    letters = list(constant)
    cat_dictionary = {'cat_name': "Charlie"}
    myList = {'Loony', 'Charlie', 'Bugs', 'Wendie', 'Ginger'}
    return render_template('basic.html', my_variable = constant, letter = letters, cat_dict = cat_dictionary, list1 = myList)    #Flask automatically looks at the same level directory for a folder named templates and then it is going to look inside the templates folder for a file named basic.html
    #The above is described as Jinja template 
if __name__ == '__main__':
    app.run(debug=True)