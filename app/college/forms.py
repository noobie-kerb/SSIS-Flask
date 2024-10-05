from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class addCollegeForm(FlaskForm):
    college_code = StringField('College Code', validators=[DataRequired()])
    college_name = StringField('College Name', validators=[DataRequired()])
    submit = SubmitField('Add College')

    def validate_college_code(self, field):
        if ' ' in field.data:
            raise ValidationError("College Code cannot contain spaces.")

class editCollegeForm(FlaskForm):
    edit_college_code = StringField('College Code', validators=[DataRequired()])
    edit_college_name = StringField('College Name', validators=[DataRequired()])
    submit = SubmitField('Edit College')

    def validate_edit_college_code(self, field):
        if ' ' in field.data:
            raise ValidationError("College Code cannot contain spaces.")

class deleteCollegeForm(FlaskForm):
    submit = SubmitField('Delete')