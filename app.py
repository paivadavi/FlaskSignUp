from flask import Flask, render_template, request
import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':qlite3
        database.signup(request.form['name'],
                        request.form['surname'],
                        request.form['age'],
                        request.form['email'],
                        request.form['password'])
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
