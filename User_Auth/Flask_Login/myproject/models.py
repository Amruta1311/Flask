from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin       #Helps get many built-in attributes 

#Adding a function that loads the current user and grab their id. So once they login we show them pages specific to their login id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)      #Getting the specific user from their id


class User(db.Model, UserMixin):    #UserMixin has all te features of logging in users and authorizing them

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)

    email = db.Column(db.String(64), unique = True, index = True)

    username = db.Column(db.String(64), unique = True, index = True)

    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):

        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    
    def check_password(self, password):

        return check_password_hash(self.password_hash, password)





