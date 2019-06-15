from basic_db import db,Puppy

#creates all the tables
db.create_all()

sam= Puppy('Sammy',3)
frank= Puppy('Frankie',5)

#at first should be none

print(sam.id)
print(frank.id)

# adding the rows to the database

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)

