#create entries into the tables

from models import db, Puppy, Owner, Toy

# creating two pups

rufus = Puppy('Rufus')

leo = Puppy('Leo')

# Add puppies to db

db.session.add_all([rufus, leo])

db.session.commit()

#Check

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()     # gives the first entry encountered whose name is rufus

print(rufus)
#rufus = Puppy.query.filter-by(name='Rufus').all()[0]  === Similar to the above line of code

#create owner object

amruta = Owner('Amruta',rufus.id)

# giving rufus toys

toy1 = Toy('ChewToy', rufus.id)

toy2 = Toy('Ball', rufus.id)

db.session.add_all([amruta, toy1, toy2])

db.session.commit()

#Grab rufus after those additions

rufus = Puppy.query.filter_by(name='Rufus').first()

print(rufus)

print(rufus.report_toys())