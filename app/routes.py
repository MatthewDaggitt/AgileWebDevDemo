from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from app import flaskApp, db
from app.forms import CreateGroupForm, LoginForm
from app.models import Group, Student


@flaskApp.route("/")
@flaskApp.route("/login", methods=['get', 'post'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)

    studentID = form.uwa_id.data
    student = Student.query.get(studentID)
    if not student:
        flash(f'No student found with ID {studentID}', 'error')
        return render_template('login.html', form=form)

    password = form.password.data
    if not student.check_password(password):
        flash(f'Invalid password. Please try again.', 'error')
        return render_template('login.html', form=form)

    login_user(student)
    return redirect(url_for('groups'))

@flaskApp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@flaskApp.route("/groups")
@login_required
def groups():
    all_groups = Group.query.all()
    return render_template('listGroups.html', groups=all_groups)


@flaskApp.route('/create')
@login_required
def create():
    form = CreateGroupForm()
    return render_template('createGroup.html', form=form)
    
@flaskApp.route('/submit', methods=['post'])
@login_required
def submit():
    form = CreateGroupForm()
    if not form.validate_on_submit():
        return render_template('createGroup.html', form=form)
    
    groupSize = int(form.groupSize.data)
    studentIDs = [
        form.student1.data,
        form.student2.data,
        form.student3.data,
        form.student4.data        
    ][:groupSize]

    students = [find_student_by_id(id) for id in studentIDs]
    if not all(students):
        return render_template('createGroup.html', form=form)
    
    all_unique = len(set(students)) == len(students)
    if not all_unique:
        flash("Groups cannot contain duplicate students!")
        return render_template('createGroup.html', form=form)

    all_free = True
    for student in students:
        if student.group:
            flash(f"{student.name} ({student.uwa_id}) is already assigned to a group")
            all_free = False

    if not all_free:
        return render_template('createGroup.html', form=form)

    group = Group()
    group.students = students

    db.session.add(group)
    db.session.commit()
    
    return redirect(location=url_for("groups"))

def find_student_by_id(id:str):
    student = Student.query.get(id)
    if not student:
        flash(f'Could not find student with UWA ID: {id}', 'error')
    return student