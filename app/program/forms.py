from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class addProgramForm(FlaskForm):
    program_code = StringField('Program Code', validators=[DataRequired()])
    program_name = StringField('Program Name', validators=[DataRequired()])
    college_code = SelectField('College', choices=[], validators=[DataRequired()])
    submit = SubmitField('Add Program')

    def validate_program_code(self, field):
        if ' ' in field.data:
            raise ValidationError("Program Code cannot contain spaces.")

    def validate_college_code(self, field):
        if ' ' in field.data:
            raise ValidationError("College Code cannot contain spaces.")

class editProgramForm(FlaskForm):
    edit_program_code = StringField('Program Code', validators=[DataRequired()])
    edit_program_name = StringField('Program Name', validators=[DataRequired()])
    college_code = SelectField('College', choices=[], validators=[DataRequired()])
    submit = SubmitField('Edit Program')

    def validate_edit_program_code(self, field):
        if ' ' in field.data:
            raise ValidationError("Program Code cannot contain spaces.")
    
    def validate_college_code(self, field):
        if ' ' in field.data:
            raise ValidationError("College Code cannot contain spaces.")


class deleteProgramForm(FlaskForm):
    submit = SubmitField('Delete')