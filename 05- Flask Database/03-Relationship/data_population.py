from model_simple import db, Puppy,Toy,Owner

# creating entries
so= Puppy('Solozo','Stray',4)
ru= Puppy('Rufus','Labra',3)
fr=Puppy('Frankie','Huskie',5)

## add puppy to the database
db.session.add_all([so,ru,fr])
db.session.commit()

## checkig
print("The entries in the Puppy table are : \n")
print(Puppy.query.all())
print("\n")

###creating the owner object ###
jose= Owner('Jose',ru.id)
ana= Owner('Ana Mickman',so.id)
ritesh=Owner('Aryan',fr.id)

### creating the toy table

t1= Toy('Chew Toy',ru.id)
t2= Toy('Ball',so.id)
t3= Toy('football',fr.id)
t4= Toy('ring bell',fr.id)
t5= Toy('basket ball',so.id)
t6= Toy('cricket ball',ru.id)

##########################################
## adding to the database ##
db.session.add_all([jose,ana,ritesh,t1,t2,t3,t4,t5,t6])
db.session.commit()

#### grabbing a random record after the aditions

soloz= Puppy.query.filter_by(name='Solozo').first()
print("\n\n")
print(soloz)
print("\n\n")
print(soloz.report_toys())



