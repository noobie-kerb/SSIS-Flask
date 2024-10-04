from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class addStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = SelectField('Program', choices=[], validators=[DataRequired()])
    year = SelectField('Year', choices =['1','2','3','4'], validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Add Student')

class editStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = StringField('Program', choices =[], validators=[DataRequired()])
    year = SelectField('Year', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Edit Student')

class deleteStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = StringField('Program', validators=[DataRequired()])
    year = SelectField('Year', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Delete Student')