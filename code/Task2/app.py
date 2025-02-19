from flask import Flask, render_template, request
from Util.get_user import get_user
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        email_hash = hashlib.sha256(email.encode("utf-8")).hexdigest()
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
        print(email_hash,password_hash)
        # user_exists, query_time = get_user(email_hash, password_hash)
        # return render_template('result.html', found=user_exists, time=query_time)

    return render_template('index.html')
