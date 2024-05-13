from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from app.blueprints import main
from app.controllers import GroupCreationError, create_group
from app.forms import CreateGroupForm, LoginForm
from app.models import Group, Student

@main.route("/")
@main.route("/login", methods=['get', 'post'])
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
    return redirect(url_for('main.groups'))

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main.route("/groups")
@login_required
def groups():
    all_groups = Group.query.all()
    return render_template('listGroups.html', groups=all_groups)


@main.route('/create')
@login_required
def create():
    form = CreateGroupForm()
    return render_template('createGroup.html', form=form)
    
@main.route('/submit', methods=['post'])
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

    try:
        create_group(studentIDs)
    except GroupCreationError as e:
        flash(e.message, 'error')
        return render_template('createGroup.html', form=form)

    return redirect(location=url_for("main.groups"))
