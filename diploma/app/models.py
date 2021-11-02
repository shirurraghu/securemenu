from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
from app import db, login_manager

class Student(UserMixin, db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	first_name = db.Column(db.String(60), index=True)
	last_name = db.Column(db.String(60), index=True)
	password_hash = db.Column(db.String(128))
	branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	is_admin = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<Student: {}>'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
	return Student.query.get(int(user_id))

class Student2(db.Model):
	__tablename__ = 'students2'
	id = db.Column(db.Integer, primary_key=True)
	regnum = db.Column(db.String(20), unique=True)
	sname = db.Column(db.String(120))
	dob = db.Column(db.DateTime)
	gender = db.Column(db.String(120))
	father = db.Column(db.String(120))
#	fmobile = db.Column(db.Integer)
#	mother = db.Column(db.String(120))
#	mmobile = db.Column(db.Integer)
	mobile = db.Column(db.Integer)
	branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
	branch = db.relationship('Branch')
	email = db.Column(db.String(120))
	caste = db.Column(db.String(120))
	address = db.Column(db.String(120))
	iamarks_id = db.Column(db.Integer, db.ForeignKey('iamarks.id'))
	semister = db.Column(db.String(150))
	fee_paid = db.Column(db.Integer)
	fee_due = db.Column(db.Integer)
	scholarship =db.Column(db.Integer)
	#library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))
	books_id = db.Column(db.Integer, db.ForeignKey('books.id'))

	def __repr__(self):
		return '<Student2: {}>'.format(self.sname)
	
	def __init__(self, regnum, sname, dob, gender, father, mobile, branch, email, caste, address, semister, fee_paid, fee_due, scholarship):
		self.regnum = regnum
		self.sname = sname
		self.father = father
		self.mobile = mobile
		self.gender = gender
		self.branch = branch
		self.email = email
		self.caste = caste
		self.address = address
		self.semister = semister
		self.fee_paid = fee_paid
		self.fee_due = fee_due
		self.dob = dob
		self.scholarship = scholarship
	
class Branch(db.Model):
	__tablename__ = 'branches'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	code = db.Column(db.String(200))
	students = db.relationship('Student', backref='branch', lazy='dynamic')
	students2 = db.relationship('Student2')
	
	def __repr__(self):
		return(self.name)

class IAMark(db.Model):
	__tablename__ = 'iamarks'
	id = db.Column(db.Integer, primary_key=True)
	sl_no = db.Column(db.Integer)
	particulars = db.Column(db.String(120))
	date = db.Column(db.DateTime)
	invigillator = db.Column(db.String(120))
	page_no = db.Column(db.Integer)
	obtained_marks = db.Column(db.Integer)
	staff_initial = db.Column(db.String(120))
	subject = db.relationship('Subject', backref='iamark', lazy='dynamic')
	students2 = db.relationship('Student2', backref='iamark', lazy='dynamic' )
	def __init__(self, students2, sl_no, particulars, date, invigillator, page_no, obtained_marks, staff_initial, subject):
		self.students2 = [students2]
		self.sl_no = sl_no
		self.particulars = particulars
		self.date = date
		self.invigillator= invigillator
		self.page_no = page_no
		self.obtained_marks= obtained_marks
		self.staff_initial=staff_initial
		self.subject = [subject]

class Subject(db.Model):
	__tablename__ = 'subjects'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250))
	iamarks_id = db.Column(db.Integer, db.ForeignKey('iamarks.id'))


	def __init__(self, name):
		self.name = name

class Book(db.Model):
	__tablename__='books'
	id = db.Column(db.Integer, primary_key=True)
	students2 = db.relationship('Student2', backref='Library', lazy='dynamic')
	book = db.relationship('Library', backref='Book', lazy='dynamic')
	issue_date = db.Column(db.DateTime)
	return_date = db.Column(db.DateTime)
	status = db.Column(db.String(120))

	def __init__(self, students2, book, issue_date, return_date, status):
		self.students2 = [students2]
		self.book = [book]
		self.issue_date = issue_date
		self.return_date = return_date
		self.status = status
	

class Library(db.Model):
	__tablename__ = 'libraries'
	id = db.Column(db.Integer, primary_key=True)
	regnum = db.Column(db.String(40))
	author = db.Column(db.String(120))
	publisher = db.Column(db.String(220))
	title = db.Column(db.String(120))
#	issue_date = db.Column(db.String(120))
#	return_date = db.Column(db.String(120))
#	status = db.Column(db.String(120))
	#students2 = db.relationship('Student2', backref='Library', lazy='dynamic')
	books_id = db.Column(db.Integer, db.ForeignKey('books.id'))

	def __init__(self, regnum, author, publisher, title):
		self.title = title
		#self.issue_date = issue_date
		self.publisher = publisher
		#self.return_date = return_date
		#self.students2 = [students2]
		self.regnum=regnum
		self.author = author
		#self.status = status
#	def __repr__(self, title, students2):
#		return self.title
#	def __init__(self, students2, title):
#		self.students2 = [students2]
#		self.title = title

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), unique=True)
	description = db.Column(db.String(200))
	students = db.relationship('Student', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role: {}>'.format(self.name)
