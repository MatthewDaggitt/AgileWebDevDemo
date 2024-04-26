from flask import redirect, render_template, request, url_for
from app import flaskApp
from app.models import Group, Student

@flaskApp.route("/")
@flaskApp.route("/groups")
def groups():
    all_groups = Group.query.all()
    return render_template('listGroups.html', groups=all_groups)


@flaskApp.route('/create')
def create():
    return render_template('createGroup.html')
    
@flaskApp.route('/submit', methods=['post'])
def submit():
    print(request.method)
    print(request.form)
    print(request.form['numberOfStudents'])
    print("Submitted!")
    return redirect(location=url_for("groups"))