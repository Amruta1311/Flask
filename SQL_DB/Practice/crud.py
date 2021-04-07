from basic import db, Kitty

#CREATE

my_kitty = Kitty('Kitkat', 6)

db.session.add(my_kitty)

db.session.commit()

#READ       ---------- ORM : Object Relational Mapper

all_kitties = Kitty.query.all()     # Returns a list of all the kitty objects in the table

print (all_kitties)

#Select by ID

kitty_one = Kitty.query.get(1)

print(kitty_one.name)

#Filter by name

kitty_charlie = Kitty.query.filter_by(name='Charlie')       # Produces some sql code that contains a list of all kitties with name Charlie which is one in our case

print(kitty_charlie.all())  #when we print this out it will print the __repr__ function 

#UPDATE

first_kitty = Kitty.query.get(2)

first_kitty.age = 1

db.session.add(first_kitty)

db.session.commit()


#DELETE

second_kitty = Kitty.query.get(2)

db.session.delete(second_kitty)

db.session.commit()

all_kitty = Kitty.query.all()
print(all_kitty)

