from flask import redirect, render_template, request, url_for
from app import flaskApp
from app.model import Group, Student

tom = Student(uwaID= "01349324", name="Tom")
jerry = Student(uwaID = "01349523", name="Jerry")  	
cardi = Student(uwaID = "01349622", name="Cardi B")  	
taylor = Student(uwaID = "01349721", name="Taylor Swift")  

group1 = Group(students=[tom, jerry, cardi, taylor])

projectGroups = [group1]

@flaskApp.route("/")
@flaskApp.route("/groups")
def groups():
    return render_template('listGroups.html', groups=projectGroups)


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