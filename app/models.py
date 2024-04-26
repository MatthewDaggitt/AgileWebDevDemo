
from typing import List
from app import db

class Student(db.Model):
    uwa_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), nullable=True)

    group = db.relationship('Group', back_populates='students')

    def __repr__(self) -> str:
        return f'<Student {self.name} {self.uwa_id}>'
    group_id
class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)

    students = db.relationship(Student, back_populates='group')
