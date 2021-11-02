from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import BranchForm, RoleForm, SubjectForm, IssueBook, StudentAssignForm, IAMarksForm, LibraryForm, Student2Form
from .. import db
from ..models import Branch, Book, Subject, Role, Student, Library, Student2, IAMark

def check_admin():
	if not current_user.is_admin:
		abort(403)

@admin.route('/branches', methods=['GET', 'POST'])
@login_required
def list_branches():
	check_admin()
	
	branches=Branch.query.all()
	return render_template('admin/branches/branches.html', branches=branches, title="Branches")

@admin.route('/libraries', methods=['GET', 'POST'])
@login_required
def list_libraries():
	check_admin()
	libraries=Library.query.all()
	return render_template('admin/libraries/libraries.html', libraries=libraries, title="Books")

@admin.route('/students2', methods=['GET', 'POST'])
@login_required
def list_students2():
	check_admin()
	students2=Student2.query.all()
	return render_template('admin/students2/students2.html', students2=students2, title="Students")

@admin.route('/branch_stud', methods = ['GET', 'POST'])
@login_required
def branch_stud():
	students2=Student2.query.all()
	return render_template('home/dashboard.html', students2=students2)




@admin.route('/libraries/add', methods=['GET', 'POST'])
@login_required
def add_libraries():
	check_admin()
	add_library = True
	form = LibraryForm()
	if form.validate_on_submit():
		library = Library(regnum=form.regnum.data, title=form.title.data, author=form.author.data, publisher=form.publisher.data)
		try:
			db.session.add(library)
			db.session.commit()
			flash('You have successfully added a new book.')
		except:
			flash('Error: book already exists.')
		return redirect(url_for('admin.list_libraries'))

	return render_template('admin/libraries/library.html', action="Add", add_library=add_library, form=form, title="Add Book")

@admin.route('/students2/add', methods=['GET', 'POST'])
@login_required
def add_students2():
	check_admin()
	add_student2 = True
	form = Student2Form()
	if form.validate_on_submit():
		student2 = Student2(regnum=form.regnum.data, sname=form.sname.data, dob=form.dob.data, gender=form.gender.data, father=form.father.data, mobile=form.mobile.data, email=form.email.data, caste=form.caste.data, address=form.address.data, semister=form.semister.data, branch=form.branch.data, fee_paid=form.fee_paid.data, fee_due=form.fee_due.data, scholarship=form.scholarship.data)
	#	try:
		db.session.add(student2)
		db.session.commit()
		flash('You have successfully added a new student.')
		#except:
		#	flash('Error: student already exists.')
		return redirect(url_for('admin.list_students2'))
	return render_template('admin/students2/student2.html', action="Add", add_student2=add_student2, form=form, title="Add Student")
			
@admin.route('/branches/add', methods=['GET', 'POST'])
@login_required
def add_branches():
	check_admin()
	add_branch = True
	form = BranchForm()
	if form.validate_on_submit():
		branch = Branch(name=form.name.data, code=form.code.data)
		try:
			db.session.add(branch)
			db.session.commit()
			flash('You have successfully added a new department.')
		except:
			flash('Error: branch name already exists.')
		return redirect(url_for('admin.list_branches'))

	return render_template('admin/branches/branch.html', action="Add", add_branch=add_branch, form=form, title="Add Department")


@admin.route('/iamarks/add', methods=['GET', 'POST'])
@login_required
def add_iamarks():
	check_admin()
	add_iamark=True
	form=IAMarksForm()
	if form.validate_on_submit():
		iamark = IAMark(sl_no=form.sl_no.data, particulars=form.particulars.data, date=form.date.data, invigillator=form.invigillator.data, page_no=form.page_no.data, obtained_marks=form.obtained_marks.data, staff_initial=form.staff_initial.data, students2=form.students2.data, subject=form.subject.data)
		db.session.add(iamark)
		db.session.commit()
		return redirect(url_for('admin.list_students2'))
		flash('You have successfully added a new Marks.')
	return render_template('admin/iamarks/iamark.html', action="Add", add_iamark=add_iamark, form=form, title="Add IA Marks")

@admin.route('/subjects')
@login_required
def list_subjects():
        subjects =Subject.query.all()
        return render_template('admin/subjects/subjects.html', subjects=subjects, title = 'Subject')

@admin.route('/subjects/add', methods=['GET', 'POST'])
@login_required
def add_subjects():
	check_admin()
	add_subject = True
	form=SubjectForm()
	if form.validate_on_submit():
		subject = Subject(name=form.name.data)
		db.session.add(subject)
		db.session.commit()
		return redirect(url_for('admin.list_subjects'))
		flash('You have successfully added a new subject.')
	return render_template('admin/subjects/subject.html', action="Add", add_subject=add_subject, form=form, title="Add Subject")

@admin.route('/subjects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_subjects(id):
	check_admin()
	add_subject=False
	subject = Subject.query.get_or_404(id)
	form = SubjectForm(obj=subject)
	if form.validate_on_submit():
		subject.name = form.name.data
		db.session.commit()
		flash('You have successfully edited the subject.')
		return redirect(url_for('admin.list_subjects'))
	form.name.data = subject.name
	return render_template('admin/subjects/subject.html', action="Edit", add_subject=add_subject, form=form, subject=subject, title="Edit Subject")


@admin.route('/branches/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_branch(id):
	check_admin()
	add_branch = False
	branch = Branch.query.get_or_404(id)
	form = BranchForm(obj=branch)
	if form.validate_on_submit():
		branch.name = form.name.data
		branch.code = form.code.data
		db.session.commit()
		flash('You have successfully edited the branch.')
		return redirect(url_for('admin.list_branches'))

	form.code.data=branch.code
	form.name.data = branch.name
	return render_template('admin/branches/branch.html', action="Edit", add_branch=add_branch, form=form, branch=branch, title="Edit Branch")

@admin.route('/students2/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student2(id):
	check_admin()
	add_student2 = False
	student2 = Student2.query.get_or_404(id)
	form = Student2Form(obj=student2)
	if form.validate_on_submit():
		student2.regnum = form.regnum.data
		student2.sname = form.sname.data
		student2.father = form.father.data
		student2.dob = form.dob.data
		student2.gender = form.gender.data
		student2.mobile = form.mobile.data
		student2.email = form.email.data
		student2.caste = form.caste.data
		student2.address = form.address.data
		student2.branch = form.branch.data
		student2.semister = form.semister.data
		student2.fee_paid = form.fee_paid.data
		student2.fee_due = form.fee_due.data
		student2.scholarship = form.scholarship.data
		db.session.commit()
		flash('You have successfully edited the student.')
		return redirect(url_for('admin.list_students2'))
	form.scholarship.data = student2.scholarship
	form.fee_due.data = student2.fee_due
	form.fee_paid.data = student2.fee_paid
	form.branch.data = student2.branch
	form.semister.data = student2.semister
	form.caste.data = student2.caste
	form.email.data = student2.email
	form.address.data = student2.address
	form.mobile.data = student2.mobile
	form.father.data = student2.father
	form.gender.data = student2.gender
	form.sname.data = student2.sname
	form.dob.data = student2.dob
	form.regnum.data = student2.regnum
	return render_template('admin/students2/student2.html', action="Edit", add_student2=add_student2, form=form, student2=student2, title="Edit Student")

@admin.route('/students2/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view_student2(id):
	check_admin()
	add_student2 = False
	student2 = Student2.query.get_or_404(id)
	iamarks = IAMark.query.get_or_404(id)
	books = Book.query.get_or_404(id)
	form2 = IssueBook(obj=books)
	form1 = IAMarksForm(obj=iamarks)
	form = Student2Form(obj=student2)
	return render_template('admin/students2/view_student.html',form2=form2, form1=form1, form=form, student2=student2)


@admin.route('/libraries/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_library(id):
	check_admin()
	add_library = False
	library = Library.query.get_or_404(id)
	form = LibraryForm(obj=library)
	if form.validate_on_submit():
		library.regnum = form.regnum.data
		library.title = form.title.data
		library.author = form.author.data
		library.publisher = form.publisher.data
		db.session.commit()
		flash('You have successfully edited the book.')
		return redirect(url_for('admin.list_libraries'))
	form.publisher.data = library.publisher
	form.author.data = library.author
	form.title.data = library.title
	form.regnum.data = library.regnum
	return render_template('admin/libraries/library.html', action="Edit", add_library=add_library, form=form, library=library, title="Edit Book")


@admin.route('/branches/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_branch(id):
	check_admin()
	branch = Branch.query.get_or_404(id)
	db.session.delete(branch)
	db.session.commit()
	flash('You have successfully deleted the branch.')

	return redirect(url_for('admin.list_branches'))

@admin.route('/subjects/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_subject(id):
	check_admin()
	subject = Subject.query.get_or_404(id)
	db.session.delete(subject)
	db.session.commit()
	flash('You have successfully deleted the subject.')
	return redirect(url_for('admin.list_subjects'))


@admin.route('/students2/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_student2(id):
	check_admin()
	student2 = Student2.query.get_or_404(id)
	db.session.delete(student2)
	db.session.commit()
	flash('You have successfully deleted the student.')
	return redirect(url_for('admin.list_students2'))


@admin.route('/libraries/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_library(id):
	check_admin()
	library = Library.query.get_or_404(id)
	db.session.delete(library)
	db.session.commit()
	flash('You have successfully deleted the book.')

	return redirect(url_for('admin.list_libraries'))


@admin.route('/roles')
@login_required
def list_roles():
	roles =Role.query.all()
	return render_template('admin/roles/roles.html', roles=roles, title = 'Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
	check_admin()
	add_role = True

	form = RoleForm()
	if form.validate_on_submit():
		role = Role(name=form.name.data, description=form.description.data)
		try:
			db.session.add(role)
			db.session.commit()
			flash('You have successfully added a new role.')
		except:
			flash('Error: role name already exists.')

		return redirect(url_for('admin.list_roles'))
	return render_template('admin/roles/role.html', add_role=add_role, form=form, title='Add Role')

@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):

	check_admin()
	add_role = False

	role = Role.query.get_or_404(id)
	form = RoleForm(obj=role)
	if form.validate_on_submit():
		role.name = form.name.data
		role.description = form.description.data
		db.session.add(role)
		db.session.commit()
		flash('You have successfully edited the role.')

		return redirect(url_for('admin.list_roles'))
	form.description.data = role.description
	form.name.data = role.name
	return render_template('admin/roles/role.html', add_role=add_role, form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
	check_admin()
	role=Role.query.get_or_404(id)
	db.session.delete(role)
	db.session.commit()
	flash('You have successfully deleted the role.')

	return redirect(url_for('admin.list_roles'))
	return render_template(title="Delete Role")

@admin.route('/students')
@login_required
def list_students():

	check_admin()

	students = Student.query.all()
	return render_template('admin/students/students.html', students=students, title="Students")

@admin.route('/students/assign/<int:id>', methods = ['GET', 'POST'])
@login_required
def assign_student(id):

	check_admin()

	student = Student.query.get_or_404(id)

	if student.is_admin:
		abort(403)

	form = StudentAssignForm(obj=student)
	if form.validate_on_submit():
		student.branch = form.branch.data
		student.role = form.role.data
		db.session.add(student)
		db.session.commit()
		flash('You have successfully assigned a branch and role.')

		return redirect(url_for('admin.list_students'))
	return render_template('admin/students/student.html', student=student, form=form, title="Assign Employee")

@admin.route('/libraries/assign', methods = ['GET', 'POST'])
@login_required
def assign_book():
	check_admin()
	form = IssueBook()
	if form.validate_on_submit():
		library = Book(book=form.book.data, status=form.status.data, students2=form.students2.data, issue_date = form.issue_date.data, return_date = form.return_date.data)
		db.session.add(library)
		db.session.commit()
		flash('You have successfully assinged a book to a student.')
		return redirect(url_for('admin.list_libraries'))
	return render_template('admin/libraries/assignbook.html',  form=form,  title="Assign Book")


		
