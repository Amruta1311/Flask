from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get('username')

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(a.isupper() for a in username)
    num_end = username[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    return render_template('report.html', report=report, lower = lower_letter, upper = upper_letter, num_end = num_end)

if __name__ == '__main__':
    app.run(debug=True)