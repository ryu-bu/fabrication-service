from models.useritem import UserItem
import datetime
from flask_jwt_extended import create_access_token


class UserControl:
    def gen_user(body):
        user = UserItem(
            email = body['email'],
            password = body['password'],
            role = 'machinist'
        )
        user.hash_password()
        user.save()

        return {'id': str(user.id)}, 200
    
    def gen_manager(body):
        user = UserItem(
            email = body['email'],
            password = body['password'],
            role = 'manager'
        )
        user.hash_password()
        user.save()

        return {'id': str(user.id)}, 200

    def get_token(body):
        user = UserItem.objects.get(email=body['email'])
        authorized = user.check_password(body['password'])
        
        if not authorized:
            return {'message': 'email or password invalid'}, 401

        expires = datetime.timedelta(minutes=10)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token, 'user': user.email, 'role': user.role}, 200

    def update_user(body):
        user = UserItem.objects.get(email=body['email'])
        user.update(
            password = body['password'],
            role = body['role']
        )
        return {"message": "update success"}, 201

    def get_role(id):
        user = UserItem.objects.get(id=id)
        return user.role 

    def get_email(id):
        user = UserItem.objects.get(id=id)
        return user.email