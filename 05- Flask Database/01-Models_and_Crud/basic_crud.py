from basic_db import db,Puppy

## Create the first step of crud ######
my_puppy= Puppy('Solozo',3)
db.session.add(my_puppy)
db.session.commit()

## Read ##
## To get the list of all the puppies in the databse
all_puppies= Puppy.query.all()
print(all_puppies)
print("\n after printing all records \n")

## select based on some attributes
puppy_one= Puppy.query.get(1)
print(puppy_one.name)
print("\n after printing all records base on some attributes \n")

### Applying Filters i.e based on some condition
puppy_f= Puppy.query.filter_by(name='Solozo')
print(puppy_f.all())
print("\n after printing all records based on some filters \n")

#### updating the data
first_p= Puppy.query.get(1)
first_p.age=10
db.session.add(first_p)
db.session.commit()

#### For deletion of a record from the table
sec_p= Puppy.query.get(1)
db.session.delete(sec_p)
db.session.commit()

## printing after alteration
all_pup= Puppy.query.all()
print(all_pup)
print("\n after printing all updation and deletion \n")