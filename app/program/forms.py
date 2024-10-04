from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class addProgramForm(FlaskForm):
    program_code = StringField('Program Code', validators=[DataRequired()])
    program_name = StringField('Program Name', validators=[DataRequired()])
    college_code = SelectField('College', choices =[], validators=[DataRequired()])
    submit = SubmitField('Add Program')

class editProgramForm(FlaskForm):
    edit_program_code = StringField('Program Code', validators=[DataRequired()])
    edit_program_name = StringField('Program Name', validators=[DataRequired()])
    college_code = SelectField('College', choices=[], validators=[DataRequired()])
    submit = SubmitField('Edit College')

class deleteProgramForm(FlaskForm):
    submit = SubmitField('Delete')