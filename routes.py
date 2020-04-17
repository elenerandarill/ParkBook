from flask import render_template, Flask, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from models import User, PkgSpace
from forms import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '2d65c65e323654552be29cc808a58eac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/login')
def login():
    return render_template('login.html', title='Log In')


@app.route('/register')
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User has been registered.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
