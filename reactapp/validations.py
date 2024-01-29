from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.http import QueryDict
import json

UserModel = get_user_model()

def custom_validation(data):
    email = data.get("email", '')
    username = data.get("username", '')
    password = data.get("password", '')
    print(email, username, password)
    ##
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('choose another email')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not username:
        raise ValidationError('choose another username')
    return data


def validate_email(data):
    email = data.get("email", '')
    print(email)
    if not email:
        raise ValidationError('an email is needed')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data.get("password", '')
    print(password)
    if not password:
        raise ValidationError('a password is needed')
    return True