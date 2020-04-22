import flask
from flask import render_template, Flask, flash, url_for, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from PbApp import pb_app, pb_db
from models import User, PkgSpace


@pb_app.route('/')
@pb_app.route('/home')
def home():
    all_spaces = PkgSpace.query.order_by(PkgSpace.number).all()
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


@pb_app.route('/addspace', methods=['GET', 'POST'])
@login_required
def add_space():
    from forms import AddSpaceForm
    form = AddSpaceForm()
    if form.validate_on_submit():
        find = PkgSpace.query.filter_by(number=form.number.data).first()
        if find:
            flash('Parking Space already exists.', 'danger')
        else:
            space = PkgSpace(number=int(form.number.data), booker='none', owner=current_user)
            pb_db.session.add(space)
            pb_db.session.commit()
            flash('Parking space created.', 'info')
            return redirect(url_for('home'))
    return render_template('addspace.html', title='Add Space', form=form)


@pb_app.route('/spaces/<int:space_id>/book', methods=['POST'])
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


@pb_app.route('/spaces/<int:space_id>/cancel_book', methods=['POST'])
@login_required
def cancel_book(space_id):
    m = flask.request.method
    space = PkgSpace.query.get_or_404(space_id)
    space.booker = 'none'
    pb_db.session.commit()
    flash('Your booking has been cancelled.', 'success')
    return redirect(url_for('home'))


@pb_app.route('/spaces/<int:space_id>/delete_pksp', methods=['POST'])
@login_required
def delete_pksp(space_id):
    space = PkgSpace.query.get_or_404(space_id)
    pb_db.session.delete(space)
    pb_db.session.commit()
    flash("Parking Space has been deleted.", "info")
    return redirect(url_for('home'))

