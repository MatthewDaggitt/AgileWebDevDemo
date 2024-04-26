from app import db
from app.models import *

group1 = Group()

tom = Student(uwa_id= "01349324", name="Tom")
jerry = Student(uwa_id = "01349523", name="Jerry")  	
cardi = Student(uwa_id = "01349622", name="Cardi B")  	
taylor = Student(uwa_id = "01349721", name="Taylor Swift")  

db.session.add_all([group1, tom, jerry, cardi, taylor])
db.session.commit()