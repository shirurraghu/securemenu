from flask import render_template, abort
from flask_login import login_required, current_user
from ..models import Student,  Student2, Branch
from . import home
from sqlalchemy import or_
from .. import db


@home.route('/')
def homepage():
	return render_template('/home/index.html', title="Welcome")

@home.route('/dashboard', )
@login_required
def dashboard():
	return render_template('home/dashboard.html',  title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
	if not current_user.is_admin:
		abort(403)
	return render_template('home/admin_dashboard.html',  title="Dashboard")


@home.route('/student_view', methods=['GET', 'POST'])
@login_required
def branch_student():
        students2 = Student2.query.all()
        #iamarks = IAMark.query.get_or_404(id)
        #books = Book.query.get_or_404(id)
        #form2 = IssueBook(obj=books)
        #form1 = IAMarksForm(obj=iamarks)
        #form = Student2Form(obj=student2)
        return render_template('home/dashboard.html', students2=students2)

#@admin.route('/students2', methods=['GET', 'POST'])
#@login_required
#def list_students2():
#        check_admin()
#        students2=Student2.query.all()
#        return render_template('admin/students2/students2.html', students2=students2, title="Students")
