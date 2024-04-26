from flask import flash, redirect, render_template, request, url_for
from app import flaskApp, db
from app.forms import GroupForm
from app.model import Group, Student


@flaskApp.route("/")
@flaskApp.route("/groups")
def groups():
    groups = Group.query.all()
    return render_template('listGroups.html', groups=groups)


@flaskApp.route('/create')
def create():
    form = GroupForm()
    return render_template('createGroup.html', form=form)
    
@flaskApp.route('/submit', methods=['post'])
def submit():
    form = GroupForm()
    if not form.validate_on_submit():
        print("Invalid form")
        return render_template('createGroup.html', form=form)
    
    members = [
        find_student_by_id(form.student1.data),
        find_student_by_id(form.student2.data),
        find_student_by_id(form.student3.data),
        find_student_by_id(form.student4.data)
    ]

    if not all(members):
        return render_template('createGroup.html', form=form)

    group = Group()
    for student in members:
        student.group = group

    db.session.add_all([group])
    db.session.commit()

    print("Created!")
    return redirect(location=url_for("groups"))

def find_student_by_id(uwa_id:str):
    result = Student.query.get(uwa_id)
    if not result:
        flash(f'Could not find student with the UWA ID: {uwa_id}', category='error')
    return result