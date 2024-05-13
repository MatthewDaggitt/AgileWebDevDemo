from app import db
from app.models import *


tom = Student(uwa_id= "01349324", name="Tom")
jerry = Student(uwa_id = "01349523", name="Jerry")  	
cardi = Student(uwa_id = "01349622", name="Cardi B")  	
taylor = Student(uwa_id = "01349721", name="Taylor Swift")  

group1 = Group()
group1.students = [tom, jerry]

def add_test_students_to_db():
    db.session.add_all([tom, jerry, cardi, taylor])
    db.session.commit() 

def add_test_group_to_db():
    db.session.add(group1)
    db.session.commit()

db.session.add_all([group1, tom, jerry, cardi, taylor])
db.session.commit()