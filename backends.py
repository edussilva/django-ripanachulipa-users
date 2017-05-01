# coding: utf-8

from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class ModelBackend(BaseModelBackend):
    '''
        Custom backend for login with username
    '''
    def authenticate(self, username=None, password=None):

        if not username is None:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
