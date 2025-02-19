from flask import Flask, render_template, request
from Util.get_user import get_user
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email_hash = request.form['email']
        password_hash = request.form['password']
        user_exists, query_time = get_user(email_hash, password_hash)
        return render_template('result.html', found=user_exists, time=query_time)

    return render_template('index.html')
