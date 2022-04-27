from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from custom_users.models import MyUser
from services.RSA_keys_manipulate import check_signature


User = get_user_model()


class AuthBackend(ModelBackend):
    """
     Custom auth backend
    """

    def authenticate(self, request, username=None, password=None, **kwargs):

        login, pubkey = username, password

        if users := MyUser.objects.filter(login=username):
            user = users[0]
            pubkey = pubkey.replace('KEY----- ', 'KEY-----\n').replace(' -----END', '\n-----END')

            try:
                check_signature(public_key=pubkey, signature=user.signature)

            except:
                return None

            else:
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
