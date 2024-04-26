from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GroupForm(FlaskForm):
    student1 = StringField('Student 1 ID', validators=[DataRequired()])
    student2 = StringField('Student 2 ID', validators=[DataRequired()])
    student3 = StringField('Student 3 ID', validators=[DataRequired()])
    student4 = StringField('Student 4 ID', validators=[DataRequired()])
    submit = SubmitField('Create group')