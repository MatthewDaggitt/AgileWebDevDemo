
from typing import List

from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app import login

class Student(db.Model, UserMixin):
    uwa_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), nullable=True)
    password_hash = db.Column(db.String(128))

    group = db.relationship('Group', back_populates='students')

    def __repr__(self) -> str:
        return f'<Student {self.name} {self.uwa_id}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.uwa_id

@login.user_loader
def get_user(id):
    return Student.query.get(id)

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)

    students = db.relationship(Student, back_populates='group')
