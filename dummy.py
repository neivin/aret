# init farmer dummy data
#app.db.session.query(app.Farmer).filter(app.Farmer.id>1).delete()

# f = app.Farmer(name='', email=email, password_hash= pw_hash, phone=phone, region=region, age=age)

import app
from passlib.apps import custom_app_context as pwd

list = ['Tennie Throckmorton','Earleen Edgemon','Brittny Bezio','Arvilla Albrecht','Leia Leake','Otilia Olsson','Georgette Galbraith','Mariam Mcdougle','Morris Meals','Demetrice Dorough','Denisha Dement','Maryetta Mcneilly','Margeret Millican','Avril Abbot','Reva Robison','Edda Emmer','Leonora Lofgren','Coleman Carbo','Greg Go','Jacques Juan']
count = 1
for name in list:
	fname = name[: name.find(' ')].lower()
	
	age = 45
	region = 2
	if count % 2 == 0 and count % 3 == 0:
		age = 30
		region = 3
	elif count % 2 == 0:
		age = 25
		region = 4

	f = app.Farmer(name=name, email=fname+'@aret.com', phone='123456', region=region, age=age)
	f.password_hash = pwd.encrypt('password')
	count+=1
	app.db.session.add(f)

app.db.session.commit()