from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Student

@auth.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		student = Student(email=form.email.data, username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=form.password.data)
		db.session.add(student)
		db.session.commit()
		flash('You hav successfully registered! You many now login.')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # check whether student exists in the database and whether
        # the password entered matches the password in the database
        student = Student.query.filter_by(email=form.email.data).first()
        if student is not None and student.verify_password(
                form.password.data):
            # log student in
            login_user(student)

            # redirect to the appropriate dashboard page
            if student.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('admin.branch_stud'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have successfully bee logged out.')

	return redirect(url_for('auth.login'))
