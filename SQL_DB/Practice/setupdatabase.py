from basic import db, Kitty

db.create_all()     #Setting up the database. Creates all the table models. Model class to db tables

charlie = Kitty('Charlie', 4)

ginger = Kitty('Ginger', 3)


# The below will print none since these entries have not yet been added to the database

print(charlie.id)

print(ginger.id)

db.session.add_all([charlie, ginger])   # Adding a list of objects into the table

db.session.commit()     # Saves the changes to the databse

print(charlie.id)

print(ginger.id)