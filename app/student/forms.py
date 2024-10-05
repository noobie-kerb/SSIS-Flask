from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,  SubmitField
from wtforms.validators import DataRequired

class addStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = SelectField('Program', choices=[], validators=[DataRequired()])
    year = SelectField('Year', validators=[DataRequired()], 
                       choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('Other', 'Other')])
    gender = SelectField('Gender', validators=[DataRequired()], 
                         choices=[('Male', 'Male'), ('Female', 'Female')])
    submit = SubmitField('Add Student')

class editStudentForm(FlaskForm):
    edit_student_id = StringField('Student ID', validators=[DataRequired()])
    edit_first_name = StringField('First Name', validators=[DataRequired()])
    edit_last_name = StringField('Last Name', validators=[DataRequired()])
    course = SelectField('Course', validators=[DataRequired()], choices=[])
    edit_year = SelectField('Edit Year', validators=[DataRequired()], 
                       choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('Other', 'Other')])
    edit_gender = SelectField('Gender', validators=[DataRequired()], 
                         choices=[('Male', 'Male'), ('Female', 'Female')])
    submit = SubmitField('Update Student')

class deleteStudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    course = StringField('Program', validators=[DataRequired()])
    year = SelectField('Year', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField('Delete Student')