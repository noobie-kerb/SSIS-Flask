from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class addCollegeForm(FlaskForm):
    college_code = StringField('College Code', validators=[DataRequired()])
    college_name = StringField('College Name', validators=[DataRequired()])
    submit = SubmitField('Add College')

class editCollegeForm(FlaskForm):
    edit_college_code = StringField('College Code', validators=[DataRequired()])
    edit_college_name = StringField('College Name', validators=[DataRequired()])
    submit = SubmitField('Edit College')

class deleteCollegeForm(FlaskForm):
    submit = SubmitField('Delete')