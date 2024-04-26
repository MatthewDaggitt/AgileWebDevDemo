from flask import flash, redirect, render_template, request, url_for
from app import flaskApp
from app.forms import CreateGroupForm
from app.models import Group, Student

@flaskApp.route("/")
@flaskApp.route("/groups")
def groups():
    all_groups = Group.query.all()
    return render_template('listGroups.html', groups=all_groups)


@flaskApp.route('/create')
def create():
    form = CreateGroupForm()
    return render_template('createGroup.html', form=form)
    
@flaskApp.route('/submit', methods=['post'])
def submit():
    form = CreateGroupForm()
    if not form.validate_on_submit():
        return render_template('createGroup.html', form=form)
    
    student1 = find_student_by_id(form.student1.data, required=True)
    student2 = find_student_by_id(form.student2.data, required=True)
    student3 = find_student_by_id(form.student3.data, required=False)
    student4 = find_student_by_id(form.student4.data, required=False)

    if not (student1 and student2):
        return render_template('createGroup.html', form=form)
    


    return redirect(location=url_for("groups"))

def find_student_by_id(id:str, required:bool):
    student = Student.query.get(id)
    if not student and required:
        flash(f'Could not find student with UWA ID: {id}', 'error')
    return student