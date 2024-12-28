from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Optional
import re
from flask_wtf.file import FileField, FileAllowed, file_required

def FileSizeLimit(max_size_in_mb):
    max_bytes = max_size_in_mb*1024*1024
    def file_length_check(form, field):
        if len(field.data.read()) > max_bytes:
            raise ValidationError(f"File size must be less than {max_size_in_mb}MB")
        field.data.seek(0)
    return file_length_check


class addStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = SelectField('Course', choices=[], validators=[DataRequired()])
    year = SelectField('Year', choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year')], validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    photo = FileField('Student Photo', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!'), FileSizeLimit(max_size_in_mb = 5)
    ])
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
    edit_photo = FileField('editPhoto', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!'), Optional()], render_kw={'id': 'editPhoto'})
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