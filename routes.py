from flask import render_template, Flask, flash, url_for, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from PbApp import pb_app, pb_db
from models import User, PkgSpace


@pb_app.route('/')
@pb_app.route('/home')
def home():
    all_spaces = PkgSpace.query.all()
    return render_template('home.html', title='Home', all_spaces=all_spaces)


@pb_app.route('/register', methods=['GET', 'POST' ])
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


@pb_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    from forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            # z modulu 'flask_login' importujemy 'login_user'
            login_user(user, remember=form.remember.data)
            # Trzeba zajac sie 'next' page ze wzgledow bezpieczenstwa.
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login failed, try again.', 'danger')
    return render_template('login.html', title='Log In', form=form)


@pb_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))





@pb_app.route('/book')
@login_required
def book(space_id):
    space = PkgSpace.query.get_or_404(space_id)
    if space.booker == 'none':
        space.booker = current_user.username
        pb_db.session.commit()
        flash('Space has been booked for you.', 'success')
    else:
        flash('Space is already booked, sorry.', 'danger')
    return redirect(url_for('home'))


@pb_app.route('/cancel_book')
@login_required
def cancel_book(space_id):
    space = PkgSpace.query.get_or_404(space_id)
    space.booker = 'none'
    pb_db.session.commit()
    flash('Your booking has been cancelled.', 'success')
    return redirect(url_for('home'))

