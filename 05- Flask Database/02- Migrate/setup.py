from basic_app import db,Puppy

#creates all the tables
db.create_all()

sam= Puppy('Sammy',3,"labra")
frank= Puppy('Frankie',5,"Huskie")

#at first should be none

print(sam.id)
print(frank.id)

# adding the rows to the database

db.session.add_all([sam,frank])

db.session.commit()

print("\n breed column added successfully...!!! \n")
print(sam.breed)
print(frank.breed)

