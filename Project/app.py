from flask import Flask, render_template, request
import re

app = Flask(__name__)

def password_check(cur):
    check = 0
    messages = []

    if not len(cur) >= 8:
        messages.append("Password should be at least 8 characters long")
        check = 1

    if not re.search('[A-Z]', cur):
        messages.append("Password must have at least one uppercase letter")
        check = 1

    if not re.search('[0-9]', cur):
        messages.append("Password must have at least one numerical value")
        check = 1

    if not re.search('[!@#$%^&*(),.?":{}|<>]', cur):
        messages.append("Password must have one or more special characters")
        check = 1

    return check, messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        check, messages = password_check(password)

        if check == 0:
            return render_template('result.html', message="Password is okay")
        else:
            return render_template('result.html', message="Password validation failed", errors=messages)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)