from secrets import randbelow, token_urlsafe
from django.conf import settings
from django.core.mail import send_mail
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six


# class TokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#             six.text_type(user.pk) + six.text_type(timestamp) +
#             six.text_type(user.is_active)
#         )
# account_activation_token = TokenGenerator()


def generate_url():
    length = randbelow(30)
    while(length < 15):
        length = randbelow(30)
    string = token_urlsafe(length)
    return string


def varification_mailto(reciever, token):
    subject = "Email varification mail from Snapshare.com"
    url = "http://localhost:8000/accounts/validate/" + token
    body = """ Thank You for Signing up with us!\n
    This is a email confermation message!\n
    This message is autogenerated! Please Do Not reply!\n
    Click on this link to varify your Email:\n\t""" + url + """\n\n
    Igonre this message if you didn't tried to signup here at Snapshare!\n\n
    Regards,\n
    Snapshare.com"""
    
    sender = "snapshare"
    user = "djangoemaildem0@gmail.com"
    password = "djang0123"
    
    try:
        send_mail(subject, body, sender, reciever, fail_silently=False, auth_user=user, auth_password=password,)
        return True
    except:
        return False
