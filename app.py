from flask import Flask, request, render_template, redirect, url_for, flash
import json
import os

app = Flask(__name__, template_folder="templates")
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user  = request.form['user']
        repo  = request.form['repo']
        weeks = request.form['weeks']
        stakeholder = request.form['stakeholder']

	# Creates the raw_output.json file

        cmd = "python GetPullRequests.py {0} {1} {2}".format(user, repo, weeks)
        os.system(cmd)

        # Assuming raw_output.json is already generated and available
        with open('raw_output.json') as f:
            data = json.load(f)

        return render_template('report.html', data=data, stakeholder=stakeholder)

    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    stakeholder = request.form['stakeholder']
    os.system(f'python send_email.py {stakeholder}')
    flash('Email has been sent successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
