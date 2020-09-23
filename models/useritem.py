from mongoengine import *
from flask_bcrypt import generate_password_hash, check_password_hash

class UserItem(Document):

    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=5)
    role = StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
        