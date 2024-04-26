from app import db
from app.model import Student, Group


group1 = Group()

tom = Student(uwa_id= "01349324", name="Tom")
db.session.add(tom)
db.session.commit()

jerry = Student(uwa_id = "01349523", name="Jerry", group=group1)  	
cardi = Student(uwa_id = "01349622", name="Cardi B", group=group1)  	
taylor = Student(uwa_id = "01349721", name="Taylor Swift", group=group1)  

db.session.add_all([tom, jerry, cardi, taylor])
db.session.add_all([group1])
db.session.commit()