from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()   #We have a instance of a hasher

mypassword = "supersecretpassword"

hashed_password = bcrypt.generate_password_hash(password = mypassword)

print(hashed_password)      #Prints the hashed version of password

check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')    # We check if the hased version of password matches with the other password that user provides as second argument

print(check)