from flask import render_template, Flask, flash, url_for, redirect

from PbApp import pb_app, pb_db
from models import User, PkgSpace


@pb_app.route('/')
@pb_app.route('/home')
def home():
    return render_template('home.html', title='Home')


@pb_app.route('/login')
def login():
    return render_template('login.html', title='Log In')


@pb_app.route('/register')
def register():
    from forms import RegistrationForm
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        pb_db.session.add(user)
        pb_db.session.commit()
        flash('User has been registered.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
