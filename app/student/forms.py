from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import re

class addStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = SelectField('Course', choices=[], validators=[DataRequired()])
    year = SelectField('Year', choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Add Student')

    def validate_student_id(self, field):
        if not re.match(r'^\d{4}-\d{4}$', field.data):
            raise ValidationError("Student ID must be in the format xxxx-xxxx (e.g., 2022-0076) with no spaces.")

class editStudentForm(FlaskForm):
    edit_student_id = StringField('Student ID', validators=[DataRequired()])
    edit_first_name = StringField('First Name', validators=[DataRequired()])
    edit_last_name = StringField('Last Name', validators=[DataRequired()])
    course = SelectField('Course', choices=[], validators=[DataRequired()])
    edit_year = SelectField('Year', choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], validators=[DataRequired()])
    edit_gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Edit Student')

    def validate_edit_student_id(self, field):
        if not re.match(r'^\d{4}-\d{4}$', field.data):
            raise ValidationError("Student ID must be in the format xxxx-xxxx (e.g., 2022-0076) with no spaces.")


class deleteStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = StringField('Program', validators=[DataRequired()])
    year = SelectField('Year', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Delete Student')