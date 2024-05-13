
from app.models import Group, Student
from app import db

class GroupCreationError(Exception):
    pass

def create_group(studentIDs):
    students = []
    missing_students = []
    for id in studentIDs:
        student = Student.query.get(id)
        if not student:
            missing_students.append(id)
        else:
            students.append(student)

    if missing_students:
        raise GroupCreationError("Not all students registered")
    
    all_unique = len(set(students)) == len(students)
    if not all_unique:
        raise GroupCreationError("Groups cannot contain duplicate students!")

    assignedStudents = []
    for student in students:
        if student.group:
            assignedStudents.append(student)

    if assignedStudents:
        message = ""
        for student in students:
            message += f"{student.name} ({student.uwa_id}) is already assigned to a group\n"
        raise GroupCreationError(message)

    group = Group()
    group.students = students

    db.session.add(group)
    db.session.commit()