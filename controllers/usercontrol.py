from models.useritem import UserItem
import datetime
from flask_jwt_extended import create_access_token


class UserControl:
    def gen_user(body):
        user = UserItem(
            email = body['email'],
            password = body['password'],
            role = body['role']
        )
        user.hash_password()
        user.save()

        return {'id': str(user.id)}, 200

    def get_token(body):
        user = UserItem.objects.get(email=body['email'])
        authorized = user.check_password(body['password'])
        
        if not authorized:
            return {'message': 'email or password invalid'}, 401

        expires = datetime.timedelta(minutes=20)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200

    def update_user(body):
        user = UserItem.objects.get(email=body['email'])
        user.update(
            password = body['password'],
            role = body['role']
        )
        return {"message": "update success"}, 201