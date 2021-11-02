from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Branch,Book, Subject, Role, Student, Library, Student2, IAMark

class BranchForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	code = StringField('Branch Code', validators=[DataRequired()])
	submit = SubmitField('Submit')

class RoleForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')

class IssueBook(FlaskForm):
	book = QuerySelectField(query_factory=lambda: Library.query.all(), get_label="regnum")
	students2 = QuerySelectField(query_factory=lambda: Student2.query.all(), get_label="sname")
	issue_date = DateField('Issue Date', validators=[DataRequired()])
	return_date = DateField('Expected Date of Return', validators=[DataRequired()])
	status = SelectField('Returned?', choices=[('Yes', 'Yes'), ('No', 'No')])
	submit=SubmitField('Issue Book')


class StudentAssignForm(FlaskForm):
	branch = QuerySelectField(query_factory=lambda: Branch.query.all(), get_label="name")
	role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label="name")
	submit=SubmitField('Submit')

class LibraryForm(FlaskForm):
	regnum = StringField('Register Number', validators=[DataRequired()])
	title = StringField('Book Name', validators=[DataRequired()])
	author = StringField('Author')
	publisher = StringField('Publisher')
	submit=SubmitField('Add')

class Student2Form(FlaskForm):
	regnum = StringField('Register Number', validators=[DataRequired()]) 
	sname = StringField('Student Name', validators=[DataRequired()])
	dob = DateField('Date of Birth', validators=[DataRequired()])
	gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')])
	father = StringField('Father Name', validators=[DataRequired()])
	mobile = IntegerField('Mobile #', validators=[DataRequired()])
	email = StringField('Email ID')
	address = StringField('Address')
	semister = IntegerField('Semister')
	branch = QuerySelectField(query_factory=lambda: Branch.query.all(), get_label="name")
	caste = StringField('Caste', validators=[DataRequired()])
	fee_paid = IntegerField('Fee Paid', validators=[DataRequired()])
	fee_due = IntegerField('Fee Due', validators=[DataRequired()])
	scholarship = IntegerField('Scholarship Amount')
	submit=SubmitField('Add')

class IAMarksForm(FlaskForm):
	sl_no = IntegerField('Serial #', validators=[DataRequired()])
	particulars = StringField('Particulars')
	date = DateField('Date')
	invigillator = StringField('Invigilator')
	page_no = IntegerField('Page #')
	obtained_marks = IntegerField('Obtained Marks')
	staff_initial = StringField('Staff Initial')
	students2 = QuerySelectField(query_factory=lambda: Student2.query.all(), get_label="sname")
	subject = QuerySelectField(query_factory=lambda: Subject.query.all(), get_label="name")
	submit=SubmitField('Add')

class SubjectForm(FlaskForm):
	name = StringField('Subject Name', validators=[DataRequired()])
	submit = SubmitField('Add')

