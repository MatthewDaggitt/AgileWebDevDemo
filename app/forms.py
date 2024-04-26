from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class CreateGroupForm(FlaskForm):
    student1 = StringField("Student 1 id", validators=[DataRequired()])
    student2 = StringField("Student 2 id", validators=[DataRequired()])
    student3 = StringField("Student 3 id")
    student4 = StringField("Student 4 id")
    submit = SubmitField("Create group")